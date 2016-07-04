# import the necessary packages
import requests
import cv2

# define the URL to our face detection API
url = "http://localhost:8000/face_detection/detect/"

# use our face detection API to find faces in images via image URL
 fingerprint = {"url": "http://www.pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg"}
r = requests.post(url, data=fingerprint).json()
print "obama.jpg: {}".format(r)