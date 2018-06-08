def updates2html(updates):
    res = '<div>'
    for key, value in updates.items():
        res += '<span>'
        res += key + ':'
        res += '</span>'

        res += '<table>'
        res += '<tbody>'
        for topic in value:
            res += '<tr>'
            res += '<td>'
            res += '<a href="%s">' % topic.url
            res += topic.title
            res += '</a>'
            res += '</td>'
            res += '<td>'
            res += '<span>'
            res += topic.posted_at
            res += '</span>'
            res += '</td>'
            res += '<td>'
            res += '<span>'
            res += topic.from_group
            res += '</span>'
            res += '</td>'
            res += '</tr>'
        res += '</tbody>'
        res += '</table>'

        res += '<br/>'
    res += '</div>'
    return res