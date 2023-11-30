import cv2 
import json 


image = "/home/dracarys/Downloads/howard.jpg"

im = cv2.imread(image)
print(im)



dic = {"image_array": (im.tolist())}

with open("req_image.json", "w") as json_file: 
    json.dump(dic, json_file) 

