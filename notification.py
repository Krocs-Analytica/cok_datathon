import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.config_loader import read_config_file

config = read_config_file()
user = config.get('email').get('user')
# pwd = os.environ.get('krocs_analytica_password')
pwd = config.get('email').get('password')
recipient = config.get('email').get('recipient')

def send_notification(title, message, medium):
    """
    Send a notification to stakeholders.
    """
    if medium == 'email':
        send_email(title, message)
    elif medium == 'slack':
        send_slack(title, message)
    else:
        raise ValueError('Medium not supported.')


def send_slack(title, message):
    """
    Send slack message to stakeholders.
    """
    print(f'''
        Slack message Sent!
        Title: {title}
        Message: {message}
    ''')


def send_email(subject, body):

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = ", ".join(TO)

    html = f"""\
        <html>
        <head></head>
        <body>
            <p>Hi!</p>
            <p>Don't panic! <em><strong>Krocs Analytica</strong></em> is just testing her code!</p>

            <p>{body}</p>

            <em><strong>powered by:</strong></em>
            <br/>
            <img src="https://user-images.githubusercontent.com/14994703/158464363-dd554e3f-ccdf-49d8-948c-f04f8971f8b4.png"/>
            </p>
        </body>
        </html>
        """
    part1 = MIMEText(body, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2) 
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, pwd)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print('successfully sent the mail')
    except Exception as e:
        print("failed to send mail", e)
