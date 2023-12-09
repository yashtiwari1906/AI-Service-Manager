git clone https://github.com/yashtiwari1906/Face-Detector.git 
python -m venv detector-env
source detector-env/bin/activate 
cd Face-Detector
pip install --upgrade pip
pip install -r requirements.txt 
python detector_driver.py
