from enum import Enum
import os 
try:
    if os.environ.get("ENV") == 'production':
        from . import production as env
    # elif os.environ.get("ENV") == 'Staging':
    #     from .staging import *
    elif os.environ.get("ENV") == 'local':
        from . import local as env
    elif os.environ.get("ENV") == 'minikube':
        from . import minikube as env
    else:
        raise RuntimeError("wrong value of ENV variable should be in [production, local]")
except Exception as e:
    raise RuntimeError("provide the correct value for ENV variabe from [production, local], export ENV=env_name")



class DataBaseConfig(Enum):
    NAME = env.NAME
    USER = env.USER
    PASSWORD = env.PASSWORD
    HOST = env.HOST
    PORT = env.PORT

class URLConfig(Enum):
    DETECTOR_URL = env.detector_url
    VERIFIER_URL = env.verifier_url

