import os 

detector_url = "http://localhost:5001/predict"
verifier_url = "http://localhost:4001/predict" 
NAME = "postgres"
USER="user1"
PASSWORD = 1234
HOST = "localhost"
PORT = os.environ.get("NGROK_PORT")
# Celery settings
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL") 
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND") 

#email settings
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS") 
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD") 