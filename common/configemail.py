#coding:utf-8

'''
功能：
    1.配置发送邮件属性
    2.读取邮件配置
    3.发送邮件
'''


import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from readConfig import ReadConfig
from email.header import *



class ConfigEmail():


    #读取ini文件配置属性
    re = ReadConfig()
    host = re.get_email('mail_host')
    sender = re.get_email('sender')
    receiver = re.get_email('receiver')
    user = re.get_email('mail_user')
    pwd = re.get_email('mail_pass')
    subject = re.get_email('subject')
    content = re.get_email('content')

    #配置邮件属性
    msg = MIMEMultipart()
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(content, 'plain', 'utf-8'))


    def config_file(self):
        #配置附件属性
        file = self.find_file()
        print(file)
        sendfile=open(file,'rb').read()
        att = MIMEText(sendfile, 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=report.html'
        self.msg.attach(att)
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver
        self.msg['Subject'] = 'Python SMTP 附件邮件测试'
        self.msg.attach(MIMEText('UI自动化报告邮件，如果想查看详情请查收附件', 'plain', 'utf-8'))


    def find_file(self):
        #查找最新文件
        current_path = os.path.dirname(os.path.abspath(__file__))
        # print('current',current_path)
        filePath = os.path.dirname(current_path) + "/" + 'testreport'
        # print('filepath',filePath)

        fileList = os.listdir(filePath)
        # print(fileList)
        fileDict = {}
        fileTime = []
        for i in fileList:
            filename = filePath + "/" + i
            iTime = os.path.getmtime(filename)
            fileTime.append(iTime)
            fileDict[iTime] = i
        # print(fileDict,fileTime)

        sendfilekey = max(fileTime)
        sendfile = fileDict[sendfilekey]
        # print(sendfile)
        sendfile = filePath + "/" + sendfile
        return sendfile


    #发送邮件
    def send_mail(self):
        try:
            r = smtplib.SMTP()
            r.connect(host=self.host)
            r.login(user=self.user,password=self.pwd)
            r.sendmail(self.sender,self.receiver,msg=self.msg.as_string())

        except Exception as msg:
            print('邮件发送失败！')
            print(msg)
        else:
            print('邮件发送成功')
        finally:
            r.close()
#
# if __name__ == '__main__':
# #     pass
# c = ConfigEmail()
# c.send_mail()