import os
import smtplib
from configparser import ConfigParser
from email.header import Header
from email.mime.text import MIMEText


def send_email(to_addr, message):
    #此处需在项目根目录下创建config.ini文件进行配置
    cfg = ConfigParser()
    cfg.read(os.path.abspath('.') + '\config.ini')
    smtp_server = cfg.get('email', 'smtp_server')
    from_addr = cfg.get('email', 'from_addr')
    password = cfg.get('email', 'password')

    msg = MIMEText(message, 'html', 'utf-8')
    msg['From'] = u'lzh <%s>' % from_addr
    msg['to'] = u'订阅者 <%s>' % to_addr
    msg['Subject'] = Header(u'杭州滨江公寓出租信息更新', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

