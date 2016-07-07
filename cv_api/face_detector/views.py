# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import cv2
import os
#from skimage.measure import structural_similarity as ssim
#import matplotlib.pyplot as plt
# define the path to the face detector
FACE_DETECTOR_PATH = "{base_path}/cascades/haarcascade_frontalface_default.xml".format(
	base_path=os.path.abspath(os.path.dirname(__file__)))


#MAKE REFACTOR
@csrf_exempt
def detect(request):

	# initialize the data to return
	data = {"success": False}
	result = False
	idPerson = 0
	print(result)
	if request.method == "POST":
		
		if request.FILES.get("image", None) is not None:
			# grab the uploaded image
			image = _grab_image(stream=request.FILES["image"])

		# otherwise, assume that a URL was passed in
		else:
			# grab the URL from the request
			url = request.POST.get("url", None)
			# if the URL is None, then return an error
			if url is None:
				data["error"] = "No URL provided."
				return JsonResponse(data)
	

			image = cv2.imread(url,0)
			imagesdb = _get_images_url()

			for image in imagesdb:
				idPerson = image.person_id
				urlimg = image.urlimage
				image = cv2.imread(url,0)
				imagedb = cv2.imread(urlimg,0)
				#idPerson = image.person
				
				#get image by url
				differences = cv2.subtract(image,imagedb)
				result = not np.any(differences)

				if result:
					break	

			#diff = cv2.subtract(image,imaget)
			#result = not np.any(diff)
		# update the data dictionary with the faces detected
		data.update({"matching": result , "id": idPerson, "success": True})
	# return a JSON response
	return JsonResponse(data)

def _get_images_url():
	from face_detector.models import Image
	return Image.objects.all()


@csrf_exempt
def getinfo(request):
	
	data = {}
	idP = request.POST.get("id", None)
	from face_detector.models import Person
	p = Person.objects.get(pk=idP)
	data.update({"name": p.name, "last_name" : p.last_name, "work": p.work,"cellphone": p.cellphone,"street":p.street,"number_house":p.number_house,"colony":p.colony,"postalcode":p.postalcode,"municipality":p.municipality,"state":p.state});
	return JsonResponse(data);

@csrf_exempt
def addperson(request):

	data = {"success": True}
	
	name = request.POST.get("name", None)
	last_name = request.POST.get("last_name",None)
	work = request.POST.get("work",None)
	cellphone = request.POST.get("cellphone",None)
	street = request.POST.get("street",None)
	number_house = request.POST.get("number_house",None)
	colony = request.POST.get("colony",None)
	postalcode = request.POST.get("postalcode",None)
	municipality = request.POST.get("municipality",None)
	state = request.POST.get("state",None)
	urlimage = request.POST.get("urlimage",None)
			
	from face_detector.models import Person
	p = Person(name=name,last_name=last_name,work=work,cellphone=cellphone,street=street,number_house=number_house,colony=colony,postalcode=postalcode,municipality=municipality,state=state)
	p.save()

	if p.id > 0:
		data.update({"message": "Person was succesfully created"})
		from face_detector.models import Image
		m = Image(urlimage=urlimage,hand="der",finger=2,person=p)
		m.save()
	else:
		data.update({"message": "Something is wrong, please contact with administrator"})

	return JsonResponse(data)


def _grab_image(path=None, stream=None, url=None):
	# if the path is not None, then load the image from disk
	if path is not None:
		image = cv2.imread(path)

	# otherwise, the image does not reside on disk
	else:	
		# if the URL is not None, then download the image
		if url is not None:
			resp = urllib.urlopen(url)
			data = resp.read()

		# if the stream is not None, then the image has been uploaded
		elif stream is not None:
			data = stream.read()

		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image