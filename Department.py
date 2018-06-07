class Department(object):

    def __init__(self, name, latest_info):
        self.name = name
        self.latest_info = latest_info

    def __str__(self):
        return '<' + self.name + ': ' + (self.latest_info if self.latest_info != None else 'None') + '>'

    __repr__ = __str__
