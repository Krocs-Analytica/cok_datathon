import os
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


# def send_email(title, message):
#     """
#     Send an email to stakeholders.
#     """
#     print(f'''
#         Email message Sent!
#         Title: {title}
#         Message: {message}
#     ''')
    


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
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except Exception as e:
        print("failed to send mail", e)