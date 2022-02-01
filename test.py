import smtplib

gmail_user = "mailtestuser626@gmail.com"
gmail_password = "123QWEzxc"

yandex_user = "mailtestuser626@yandex.ru"
yandex_password = "123QWEzxc"

sent_from = yandex_user
to = ['ilya.v.sapunov@gmail.com',]
subject = 'Homework'
body = 'Chto po mateshe?'


{
  "server_name": "google",
  "server_login": "mailtestuser626@gmail.com",
  "server_password": "123QWEzxc",
  "sender": "i.sapunov@idaproject.com",
  "recipient": "ilya.v.sapunov@gmail.com",
  "subject": "Homework",
  "body": "Chto po mateshe?"
}


email_text = """\
From: {}
To: {}
Subject: {}

{}
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.ehlo()
    server.login(yandex_user, yandex_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except Exception as e:
    print(e)
    print('Something went wrong...')