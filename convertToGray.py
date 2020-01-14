from PIL import Image
import face_recognition
import os
import numpy
count = 1
for file in os.listdir("dataset"):
		for image_file in os.listdir("dataset/"+file+"/"):
			full_file_path = os.path.join("dataset/"+file+"/", image_file)
			image = Image.open(open(full_file_path,'rb'))
			pil_image = image.convert('L') #convert to gray scale
			pil_image = pil_image.rotate(-90)#
			newPath = "result/" + str(file)
			if not os.path.exists(newPath):
				os.makedirs(newPath)

			pil_image.save("result/" + str(file) + '/' + str(count) + ".jpg")
			count = count + 1
		count = 1
