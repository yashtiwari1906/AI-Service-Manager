from time import sleep
import json 
from celery import shared_task
from django.db import connection
import smtplib
from email.message import EmailMessage

from ai_service_manager.config.constants import EmailConfig

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
    EMAIL_ADDRESS = EmailConfig.EMAIL_ADDRESS.value
    EMAIL_PASSWORD = EmailConfig.EMAIL_PASSWORD.value
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
        send_email("hurray!!!","message successful", "yash.tiwari@cars24.com")
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


@shared_task() 
def insert_into_DB(data_dict, table):
    column_names = list(data_dict.keys()) 
    values = list(data_dict.values())
    id, name, embedding = 'id', 'name', 'embedding'
    query_str = f"insert into {table} ("+str(id)+','+str(name)+','+str(embedding)+f") values {tuple(values)}" #make a function and return a value
    # try:
    with connection.cursor() as cursor:
        cursor.execute(query_str)

    print(f"Item with id: {data_dict['id']} and name: {data_dict['name']} are saved successfully in the table {table}")