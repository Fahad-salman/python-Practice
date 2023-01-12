import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
# my_email = input('Email address Here : ')
# password = input('Password Here : ')
my_email = 'Your email'
password = 'Your password'


email = EmailMessage()
email['from'] = 'whatever'
email['to'] = '(any-email-you-want)@gmail.com'
email['subject'] = 'Important .'

email.set_content(html.substitute({
    'company_name':'blabla-org',
    'name': 'Fahad',
    }),'html')

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(my_email,password)
        smtp.send_message(email)
        print('all good !')
except Exception as e:
    print(e)