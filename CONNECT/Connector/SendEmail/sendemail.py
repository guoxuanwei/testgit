import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import configparser
import os


class SendEmail:
    # 读取配置文件
    conf = configparser.ConfigParser()
    dirname = os.path.join(os.path.dirname(__file__), 'ConFing')
    conf.read(dirname + r'\conf.ini', encoding='utf-8')

    # 发送者账号
    sender = conf.get('qq_send', 'sender_account')
    # 接收者账号
    receiver = conf.get('qq_send', 'receiver')
    receiver = receiver.split(',')

    def __init__(self):
        self.con = smtplib.SMTP_SSL('smtp.qq.com', '465')
        self.con.login(SendEmail.conf.get('qq_send', 'sender_account'),
                       SendEmail.conf.get('qq_send', 'sender_code'))

    def send_email(self, path):
        # 发送文件  附件
        # 实例化附件  创建一个信封
        message = MIMEMultipart()
        # 读取文件内容
        f = open(path, 'rb').read()
        # 读取出来的内容写在文本中
        file = MIMEText(f, 'base64', 'utf-8')
        # 纸取个名字
        file['Content-Type'] = 'application/octet-stream'
        # 信封取个名字 附件名  有个html文件发送
        file.add_header("Content-Disposition", "attachment",
                        filename=('gbk', '', SendEmail.conf.get('qq_send', 'file_name')))

        # 把纸放在信封中去
        message.attach(file)
        msg = MIMEText(SendEmail.conf.get('qq_send', 'email_message'), 'plain', 'utf-8')
        message.attach(msg)

        # 头部内容
        # 标题
        message['Subject'] = Header(SendEmail.conf.get('qq_send', 'email_title'))
        message['From'] = SendEmail.sender
        message['to'] = ';'.join(SendEmail.receiver)
        try:
            self.con.sendmail(SendEmail.sender, SendEmail.receiver, message.as_string())
            print('发送成功')
        except BaseException as e:
            print(f'发送邮件失败{e}')


if __name__ == '__main__':
    send = SendEmail()
    send.send_email(r'E:\CONNECT\Connector\report\2021-11-15 13-57-46\report.html')
