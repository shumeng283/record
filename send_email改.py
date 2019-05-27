#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
#import socks
#import socket

class SendMail():
    def send_mail(self,subject,content=None):
        #socks.set_default_proxy(socks.HTTP, addr='proxy1.bj.petrochina', port=8080)
        #socket.socket = socks.socksocket
        msg_from = '527522643@qq.com'  # 发送方邮箱
        passwd = 'mjfecfkukqrbbicj'  # 填入发送方邮箱的授权码
        msg_to = ['shumeng283@163.com']  # 收件人邮箱
        #subject = 'HSE2.0海外子系统-首页预警'  # 主题
        #content = '11'  # 正文
        msg = MIMEMultipart(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = ','.join(msg_to)
        msg.attach(MIMEText('python附件邮件测试'))
        att1 = MIMEApplication(open('C:/Users/lixh/Desktop/按时看到.txt', 'rb').read())
        att1.add_header(
                'Content-Disposition',
                'attachment', filename=('gbk', '', 'python附件邮件测试'))
        msg.attach(att1)
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("发送成功")
        except smtplib.SMTPException:
            print("发送失败")

a = SendMail().send_mail("测试")
