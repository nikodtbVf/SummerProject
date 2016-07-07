# import the necessary packages
import requests
import cv2

# define the URL to our face detection API
url = "http://localhost:8000/face_detection/detect/"

# use our face detection API to find faces in images via image URL
payload = {"url": "templateimagen.jpg", "urltwo" : "templateimagentwooo.jpg"}
r = requests.post(url, data=payload).json()
print "{}".format(r)