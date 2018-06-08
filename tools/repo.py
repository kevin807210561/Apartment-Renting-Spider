import codecs
from models.Department import Department


def get_departments():
    with codecs.open('departments/departments.txt', 'r', 'utf-8') as f:
        departments = f.readlines()
    departments = [line.strip().split('::') for line in departments]
    return [Department(department[0], department[1]) if len(department) > 1 else Department(department[0], None) for department in departments]


def save_departments(departments):
    with codecs.open('departments/departments.txt', 'w', 'utf-8') as f:
        for department in departments:
            line = department.name + '::' + department.last_pulled_at + '\n'
            f.write(line)