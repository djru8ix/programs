import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
fromaddr = input("Enter sending email address: ")
password = input("Enter password: ")
toaddr = input("Enter receiving email address: ")
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "doge_bread"
with open('/Users/LucasColley/Python/mail_bot/doge_bread.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='doge_bread.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='doge_bread.jpg')
    mime.add_header('X-Attachment-Id', '0')
    mime.add_header('Content-ID', '<0>')
    mime.set_payload(f.read())
    email.encoders.encode_base64(mime)
    msg.attach(mime)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, password)
for i in range(10):
    server.sendmail(fromaddr, toaddr, text)
