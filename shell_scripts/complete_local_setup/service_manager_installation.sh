sleep 50s
git clone https://github.com/yashtiwari1906/AI-Service-Manager.git
python -m venv service-manager-env
source service-manager-env/bin/activate 
cd AI-Service-Manager
pip install --upgrade pip
pip install -r requirements.txt 
python manage.py runserver 0.0.0.0:5050
