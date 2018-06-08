class Department(object):

    def __init__(self, name, last_pulled_at):
        self.name = name
        self.last_pulled_at = last_pulled_at

    def __str__(self):
        return '<' + self.name + ': ' + (self.last_pulled_at if self.last_pulled_at is not None else 'None') + '>'+ '\n'

    __repr__ = __str__
