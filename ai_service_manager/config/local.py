import os 

detector_url = "http://localhost:5001/predict"
verifier_url = "http://localhost:4001/predict" 
NAME = "postgres"
USER="user1"
PASSWORD = 1234
HOST = "localhost"
PORT = 5432
# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

#email settings
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS") 
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD") 