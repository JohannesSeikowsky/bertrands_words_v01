# email_util
import smtplib
import os

def send_email(subject, content):
	mail = smtplib.SMTP("smtp.gmail.com", 587)
	mail.ehlo()
	mail.starttls()

	gmail_acc = os.environ['EMAIL_ACC']
	gmail_pw = os.environ['EMAIL_PW']
	mail.login(gmail_acc, gmail_pw)

	msg_content = "Subject:{}\n\n{}".format(subject, content)
	mail.sendmail(gmail_acc, gmail_acc, msg_content)
	mail.close()