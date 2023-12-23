from time import sleep
import json 
from celery import shared_task

import smtplib
from email.message import EmailMessage

def return_html(msg):
    html = """

    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello, World!</title>
    </head>
    <body>
     """+ \
     msg + \
     """
    </body>
    </html>
    """

    return html

def send_email(title, message, email):
    with open("api/user/documents/credentials.json", "r") as json_file: 
        email_credential_dict = json.load(json_file)
    EMAIL_ADDRESS = email_credential_dict["email_address"]
    EMAIL_PASSWORD = email_credential_dict["password"]
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    html = return_html(message)
    msg.set_content(html, subtype = "html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
            
    print("email sent!!!")

@shared_task()
def send_feedback_email_task(msg):
    
    
    """
    Firstly you need to remove two factor authentication from your email and a paasword would be generated you have to use that for sending emails
    """
    # sender = "senders@email.com"
    # receivers = ['recievers@gmail.com']

    # message = """From: From Person <yashtiwari1906@gmail.com>
    # To: To Person <yashtiwari.media@gmail.com>
    # Subject: SMTP e-mail test
    # """  + msg + \
    # """
    # This is a test e-mail message.
    # """

    try:
        sleep(20)  
        print("Successfully sent email")
    except Exception as e:
        print("Error: unable to send email", e)
     # Simulate expensive operation that freezes Django
    # send_mail(
    #     "Your Feedback",
    #     f"\t{message}\n\nThank you!",
    #     "support@example.com",
    #     [email_address],
    #     fail_silently=False,
    # )


    