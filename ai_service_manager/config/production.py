import os 

detector_url = "http://detector:5001/v2/models/detector-model/infer"
verifier_url = "http://verifier:4001/v2/models/verifier-model/infer" 
NAME = "postgres"
USER="user1"
PASSWORD = 1234
HOST = "pgvector-db"
PORT = 5432
# Celery settings
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL") 
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND") 

#email settings
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS") 
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD") 