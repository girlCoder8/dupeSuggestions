import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender = 'barb.gordon@bcforward.com'
receiver = 'barb.gordon@bcforward.com'

msg = MIMEMultipart()

msg['Subject'] = 'Test mail with file attachment'
msg['From'] = 'sender'
msg['To'] = 'receiver'

filename = 'wordsTest.txt'
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))

part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)

user = 'username'
password = 'password'

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("Successfully sent email to you!")
