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


def send_email(title, message):
    """
    Send an email to stakeholders.
    """
    print(f'''
        Email message Sent!
        Title: {title}
        Message: {message}
    ''')
    


def send_slack(title, message):
    """
    Send slack message to stakeholders.
    """
    print(f'''
        Slack message Sent!
        Title: {title}
        Message: {message}
    ''')
    