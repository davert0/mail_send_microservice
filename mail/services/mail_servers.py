from abc import ABC
from http import server
from re import sub
import smtplib

EMAIL_TEXT = """\
From: {}
To: {}
Subject: {}

{}
""" 

class MailServer(ABC):
    def __init__(self, smpt_server, port) -> None:
        self.server = smtplib.SMTP_SSL(smpt_server, port)
        self.server.ehlo()
    def authenticate(self, user, password):
        try:
            self.server.login(user, password)
        except:
            print('Something went wrong...')
    def send_mail(self, sent_from, to, subject, body):
        email_text = EMAIL_TEXT.format(sent_from, to, subject, body)
        try:
            self.server.sendmail(sent_from, to, email_text)
            self.server.close()
            print('Email sent!')
        except:
            print('Something went wrong...')
