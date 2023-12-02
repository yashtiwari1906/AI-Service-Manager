from enum import Enum
import json
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
import requests
import cv2
import numpy as np 
from PIL import Image 
from django.views.decorators.csrf import csrf_exempt
from time import gmtime, strftime
from api.chehra.db import DBOperations
from api.chehra.preLoadOnStartUp import ChehraStartupHandler

def my_custom_sql(request):
	# with connection.cursor() as cursor:
	#     cursor.execute("insert into embeddingsStorage (id, name, embedding) values (100, 'check', '[1, 2, 3]');")
	#     # row = cursor.fetchall()
	db = DBOperations("embeddingsStorage")
	row = db.insert({"id":'18165053', "name":'yash', "embeddings":'[0, 0, 0]'})
	return JsonResponse({"row": "row"})

# class URLs(Enum):
# 	DETECTOR_URL = "https://127.0.0.1:5001/predict/"
# 	VERIFY_URL = "https://127.0.0.1:4001/predict/"


class FaceOperations:
	def __init__(self) -> None:
		self.detector_url = "http://127.0.0.1:5001/predict"
		self.verifier_url = "http://127.0.0.1:4001/predict"
	
	def crop_face_from_frame(self, image, save_image_with_bbox=False):
		
		headers = {
		'Content-Type': 'application/json'
		}
		payload = json.dumps({"image_array": image.tolist()})
		response = requests.request("POST", self.detector_url, headers=headers, data=payload)

		res_dict = response.json()
		coordinates = res_dict["coordianates"]
		if len(coordinates)>1:
			return None 
		p1, p2 = coordinates[0][0], coordinates[0][1]
		#cutting out face from image 
		x0, y0, x1, y1 = map(int, [p1[0], p1[1], p2[0], p2[1]])
		im = np.array(image[x0:x1,y0:y1,:])
		if save_image_with_bbox:
			output = cv2.rectangle(image,(x0, y0), (x1, y1), (255,25, 0), thickness=3)
			cv2.imwrite(strftime("%Y-%m-%d %H:%M:%S", gmtime())+"_image.jpg", output)
		return im 

	def get_face_embeddings(self, face_fame):
		headers = {
		'Content-Type': 'application/json'
		}
		payload = json.dumps({"image_array": face_fame.tolist()})
		response = requests.request("POST", self.verifier_url, headers=headers, data=payload)

		res_dict = response.json()
		embedding = res_dict["embedding"]

		return embedding
	

class RegisterFace(FaceOperations): 
	def __init__(self) -> None:
		super().__init__()

	def preprocess_image(self, image):
		pass 

	def push_embeddings_to_db(self, embedding, name):
		id = ChehraStartupHandler.get_curr_instance().get_curr_uuid()  #if you'll not put get_curr_instance then a new instance will be created 
		db = DBOperations("embeddingStore")
		column_value_dict = {"id": id, "name": name, "embedding": str(embedding)}
		res = db.insert(column_value_dict)
		return res

	def register(self, request):
		# if 'file' not in request.FILES:
		#     return 'No file part'
		
		file = request.FILES['file']
		name = request.POST.get("name", "unknown")
		img = Image.open(file).convert('RGB')
		image = np.array(img)
	
		# if self.crop_face_from_frame(image)==None:
		#     return JsonResponse({"success": False, "msg": "Multiple faces detected in the frame..."})
		
		face_frame = self.crop_face_from_frame(image)
		if face_frame is None:
			return JsonResponse({"success": False, "msg": "Multiple faces detected in the frame..."})
			
		face_frame = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB) 
		embedding = self.get_face_embeddings(face_frame) 
		res = self.push_embeddings_to_db(embedding[0], name)
		return JsonResponse({"success": True, "msg": f"face saved successfully for identity {name}"})
		

class VerifyFace(FaceOperations):
	def __init__(self) -> None:
		super().__init__()
		self.embedding = None 
		self.table = "embeddingStore"
		self.threshold_cos_sim = 0.65
		self.verification_validation_passed = True 

	def preprocess_image(self):
		pass 
	
	def search_top_k_faces_in_db(self,  k=10):
		db = DBOperations("embeddingStore")
		query = f"SELECT 1 - (embedding <=> '{self.embedding}') AS cosine_similarity, name, id FROM {self.table} ORDER BY cosine_similarity DESC LIMIT {k};"
		rows = db.similarity_search_retireval(query)
		return rows


	def get_face_identity(self, fetched_rows):
		identity = None 
		identity_cos_sim = 0
		identity_id = None 
		recognized = True 

		for row in fetched_rows:
			cosine_similarity, name, id = row
			if cosine_similarity > identity_cos_sim:
				identity_cos_sim = cosine_similarity 
				identity = name 
				identity_id = id 
		
		if identity_cos_sim < self.threshold_cos_sim: 
			identity_id, identity, identity_cos_sim, recognized = None, None, None, False 

		return (identity_id, identity, identity_cos_sim, recognized) 
		
			

	def set_embedding(self, image):
		face_frame = self.crop_face_from_frame(image, save_image_with_bbox=False)
		if face_frame is None:
			self.verification_validation_passed = False 
			return 
		face_frame = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB) 
		self.embedding = self.get_face_embeddings(face_frame)[0]
		return

	def verify(self, request):
		file = request.FILES['file']
		
		img = Image.open(file).convert('RGB')
		image = np.array(img)

		self.set_embedding(image)
		if not self.verification_validation_passed:
			return JsonResponse({"success": False, "msg": "Multiple faces detected in the frame..."})
		rows = self.search_top_k_faces_in_db()
		identity_id, identity, identity_cos_sim, recognized = self.get_face_identity(rows)
		
		return JsonResponse({"success": True, "recognized": recognized, "identity": identity, "confidence_score": identity_cos_sim})
		


@csrf_exempt
def register_face(request):
	rf_engine = RegisterFace()
	response = rf_engine.register(request) 
	return response 

@csrf_exempt
def verify_face(request): 
	vf_engine = VerifyFace() 
	response = vf_engine.verify(request)
	return response 

