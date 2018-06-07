import codecs
from Department import Department


def get_departments():
    with codecs.open('departments.txt', 'r', 'utf-8') as f:
        departments = f.readlines()
    departments = [line.strip().split('::') for line in departments]
    return [Department(department[0], department[1]) if len(department) > 1 else Department(department[0], None) for department in departments]


def get_department_info(department):
    pass


def analyse_department_page(page):
    pass


print(get_departments())