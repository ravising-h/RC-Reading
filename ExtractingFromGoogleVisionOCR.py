def GoogleOCR(Path_Of_Images, Path_Of_text):
	from google.cloud import vision
	from tqdm import tqdm
	import os
	import io
	#import argparse
	# parser = argparse.ArgumentParser()
	# parser.add_argument("Path_Of_Images")
	# parser.add_argument("Path_Of_text")
	# args = parser.parse_args()


	string = ""
	print("Image OCR at Work....")
	for image_uri in tqdm(os.listdir(Path_Of_Images)):

		client = vision.ImageAnnotatorClient()

		with io.open(os.path.join(Path_Of_Images , image_uri), 'rb') as image_file:
			content = image_file.read()

		image = vision.types.Image(content=content)
		response = client.image_properties(image=image)
		response = client.text_detection(image=image)

		for text in response.text_annotations:
			string += str(text.description)

		with open(os.path.join(Path_Of_text,image_uri[:-3] + "txt"),"w", encoding="utf-8") as file:
			file.write(string)
			string = ""

	print("Work Done!")

			