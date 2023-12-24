import os 

detector_url = "http://detector-service:5001/predict"  #in kubernetes we use port of service which is connected to the pod where are container is running 
verifier_url = "http://verifier-service:4001/predict" 
NAME = "postgres"
USER="user1"
PASSWORD = 1234
HOST = "0.tcp.in.ngrok.io"
PORT = os.environ.get("NGROK_PORT")  #this port keeps changing in ngrok
# Celery settings
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL") 
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND") 

#email settings
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS") 
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD") 