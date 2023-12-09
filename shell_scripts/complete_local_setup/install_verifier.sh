git clone https://github.com/yashtiwari1906/Face-Verifier.git 
python -m venv verifier-env
source verifier-env/bin/activate 
cd Face-Verifier
pip install --upgrade pip
pip install -r requirements.txt 
python verifier_driver.py
