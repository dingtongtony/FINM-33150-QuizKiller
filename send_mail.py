# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(title="Quiz Alert", content="", From = "Quiz Alert", To = ""):  
	server = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
	server.login("xxx", "yyy")# xxx is sender address. yyy is your password.

	main_msg = MIMEMultipart()

	##################  正    文  ###################

	text_msg = MIMEText(content)
	main_msg.attach(text_msg)


	# 设置根容器属性
	main_msg['From'] = From
	main_msg['To'] = ','.join(To)  # 群发邮件用
	main_msg['Subject'] = title  ############################   邮件标题   #######################

	fullText = main_msg.as_string()

	# 用smtp发送邮件
	try:
	    server.sendmail(From, To, fullText)
	    print('send finish')
	except:
	    print('send fail')
	finally:
	    server.quit()
