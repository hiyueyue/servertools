#!/usr/bin/env python
# -*- coding: gbk-*-
import smtplib
from email.mime.text import MIMEText
#############
mailto_list=["yuechen@lichisoft.com","569116141@qq.com"]
#####################
#mail_host="smtp.gmail.com:587"
#mail_host="smtp.126.com"
mail_host="smtp.exmail.qq.com"
mail_user="watchdog@lichisoft.com"
mail_pass="lichi2015"
mail_postfix="lichisoft.com"
######################
def send_mail(to_list,sub,content):
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,'html','utf8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP_SSL(mail_host, 465)
        #s.esmtp_features['auth'] = 'LOGIN DIGEST-MD5 PLAIN'
        print 'connecting'
        #s.connect(mail_host)
        print 'connected'
        #s.starttls()
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

'''
if send_mail(mailto_list,"test","test_python_send_mail"):
	print "send mail success"
else:
	print "send mail fail"
    '''
