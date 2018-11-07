import os
from configparser import ConfigParser

import requests  
from bs4 import BeautifulSoup

from spider import build_url, analyse_department_page, get_department_topics, spider, get_url
from models.Department import Department
from tools.repo import get_departments
from tools.updates2html import updates2html

cfg = ConfigParser()
cfg.read(os.path.abspath('.') + '\config.ini')
print(cfg.sections())
smtp_server = cfg.get('email', 'smtp_server')
from_addr = cfg.get('email', 'from_addr')
password = cfg.get('email', 'password')
print(smtp_server)
print(from_addr)
print(password)



cookies = cfg.items('douban_cookie')
print(dict(cookies))


print(get_departments())
url = build_url('滨兴小区', 0)
print(BeautifulSoup(get_url(url).content, 'html.parser').get_text())
print(BeautifulSoup(get_url(url).content, 'html.parser').get_text())
print(analyse_department_page(requests.get(url).content))
print(get_department_topics(Department('白金海岸', '2018-06-05 19:18:53')))
res = spider(get_departments())
print(updates2html(res))
print(os.path.abspath('.') + '\config.ini')
 
