from email.message import EmailMessage
import smtplib

email=EmailMessage()
email['from']='davidoff'
email['to']='rohithuppalapati77@gmail.com'
email['subject']='Our family reunion'

email.set_content('hello greetings from davidoff')

server=smtplib.SMTP(host='smtp.gmail.com',port=587)
server.ehlo()
server.starttls()
server.login('david7330654748@gmail.com','rohith1414')
server.send_message(email)

print('mail sent !!!!!')



