import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)


def send_email(email, name):
    content = Content("text/plain", BODY.format(name))
    msg = Mail(Email('i@a.com'), SUBJECT, Email(email), content)
    response = sg.client.mail.send.post(request_body=msg.get())


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
