import os 

detector_url = "http://detector-service:5000/predict"  #in kubernetes we use port of service which is connected to the pod where are container is running 
verifier_url = "http://verifier-service:4000/predict" 
NAME = "postgres"
USER="user1"
PASSWORD = 1234
HOST = "0.tcp.in.ngrok.io"
PORT = os.environ.get("NGROK_PORT")  #this port keeps changing in ngrok