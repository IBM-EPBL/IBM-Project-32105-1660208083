import smtplib
import sendgrid as sg
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "personal expense tracker"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    from_email = Email("anisha1512m@gmail.com") 
    to_email = To(email) 
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)
    try:
        sg=SendGridAPIClient('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')
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)