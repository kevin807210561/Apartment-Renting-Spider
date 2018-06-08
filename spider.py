import time
import requests
from bs4 import BeautifulSoup
from models.Topic import Topic
from tools.mail import send_email
from tools.repo import get_departments, save_departments
from tools.updates2html import updates2html


def build_url(department, start):
    return 'https://www.douban.com/group/search?start=' + str(start) + '&cat=1013&sort=time&q=' + department


def analyse_department_page(page):
    soup = BeautifulSoup(page, 'html.parser')
    topics_div = soup.find('div', class_='topics')
    topics = topics_div.find_all('tr') if topics_div is not None else []

    res = []
    for topic in topics:
        topic_attrs = topic.find_all('td')
        title = topic_attrs[0].a.get_text()
        url = topic_attrs[0].a.get('href')
        posted_at = topic_attrs[1].get('title')
        from_group = topic_attrs[3].a.get_text()
        res.append(Topic(title, posted_at, from_group, url))
    return res


def get_department_topics(department):
    res = []
    last_pulled_at = department.last_pulled_at

    if last_pulled_at is None:
        page = requests.get(build_url(department.name, 0)).content
        res = analyse_department_page(page)
    else:
        start = 0
        topics = analyse_department_page(requests.get(build_url(department.name, start)).content)
        while len(topics) > 0 and topics[-1].posted_at > last_pulled_at:
            res += topics
            start += 50
            topics = analyse_department_page(requests.get(build_url(department.name, start)).content)
        res += topics
        #删除掉末尾的已经获取过的topics
        while len(res) > 0 and res[-1].posted_at <= last_pulled_at:
            res.pop()

    #更新最近获取时间
    if len(res) > 0:
        department.last_pulled_at = res[0].posted_at

    return res


def spider(departments):
    res = {}

    for department in departments:
        topics = get_department_topics(department)
        if len(topics) > 0:
            res[department.name] = topics

    return res


if __name__ == '__main__':
    while 1:
        departments = get_departments()
        updates = spider(departments)
        if len(updates) > 0:
            print('Received new updates...')
            print('Sending...')
            send_email('151250094@smail.nju.edu.cn', updates2html(updates))
            print('Finish sending...')
            print('Time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        save_departments(departments)
        time.sleep(60 * 5)
