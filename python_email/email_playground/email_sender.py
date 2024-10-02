import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())


email = EmailMessage()
email['from'] = 'Mickey Arnold'
email['to'] = 'mickeyarnold53'
email['subject'] = 'You won money'

email.set_content(html.substitute(name='TinTin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com' ,port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('mickeyarnold53@yahoo.com', 'password')
  smtp.send_message(email)
  print('all good boss!')