class Topic(object):

    def __init__(self, title, posted_at, from_group, url):
        self.title = title
        self.posted_at = posted_at
        self.from_group = from_group
        self.url = url

    def __str__(self):
        return '<' + self.title + ', ' + self.posted_at + ', ' + self.from_group + ', ' + self.url + '>' + '\n'

    __repr__ = __str__