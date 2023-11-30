from enum import Enum
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
import requests
import cv2
import numpy as np 
from PIL import Image 
from django.views.decorators.csrf import csrf_exempt

def my_custom_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM embeddings")
        row = cursor.fetchall()

    return JsonResponse({"row": row})

class URLs(Enum):
    DETECTOR_URL = "https://127.0.0.1:5001/predict/"
    VERIFY_URL = "https://127.0.0.1:4001/predict/"

class RegisterFace: 
    def __init__(self) -> None:
        pass 
    
    def preprocess_image(self, image):
        pass 

    def crop_face_from_frame(self, image):
        
        headers = {
        'Content-Type': 'application/json'
        }
        payload = json.dumps({"image_array": image.tolist()})
        response = requests.request("POST", "http://127.0.0.1:5001/predict", headers=headers, data=payload)

        res_dict = response.json()
        coordinates = res_dict["coordianates"]
        if len(coordinates)>1:
            return None 
        p1, p2 = coordinates[0][0], coordinates[0][1]
        #cutting out face from image 
        x0, y0, x1, y1 = map(int, [p1[0], p1[1], p2[0], p2[1]])
        im = np.array(image[x0:x1,y0:y1,:])
        return im 
            
    

    def get_face_embeddings(self, face_fame):
        headers = {
        'Content-Type': 'application/json'
        }
        payload = json.dumps({"image_array": face_fame.tolist()})
        response = requests.request("POST", "http://127.0.0.1:4001/predict", headers=headers, data=payload)

        res_dict = response.json()
        embedding = res_dict["embedding"]

        return embedding

    def push_embeddings_to_db(self):
        pass 

    def register(self, request):
        print(request.POST.get("file"))
        if 'file' not in request.FILES:
            return 'No file part'
        
        file = request.FILES['file']
        
        img = Image.open(file).convert('RGB')
        image = np.array(img)
    
        # if self.crop_face_from_frame(image)==None:
        #     return JsonResponse({"success": False, "msg": "Multiple faces detected in the frame..."})
        
        face_frame = self.crop_face_from_frame(image)
        embedding = self.get_face_embeddings(face_frame) 

        return JsonResponse({"success": True, "msg": "face saved successfully..."})
        

class VerifyFace:
    def __init__(self) -> None:
        pass

    def preprocess_image(self):
        pass 

    def get_face_embeddings(self):
        pass 

    def search_top_k_faces_in_db(self,  k):
        pass 

    def get_face_identity(self):
        pass 

@csrf_exempt
def register_face(request):
    rf_engine = RegisterFace()
    response = rf_engine.register(request) 
    return response 

def verify_face(request): 
    pass 

