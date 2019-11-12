def Tesseract(Path_Of_Images,Path_Of_text):
	from PIL import Image
	import pytesseract
	import os
	from tqdm import tqdm
	#import argparse

	# parser = argparse.ArgumentParser()
	# parser.add_argument("Path_Of_Images")
	# parser.add_argument("Path_Of_text")
	# args = parser.parse_args()
	Text_path  = Path_Of_text  + "/"
	Image_path = Path_Of_Images + "/"
	Text_Extn  = ".txt"
	if not(os.path.exists(Text_path)):
		os.mkdir(Text_path)
	image_list = os.listdir(Image_path)
	print("Reading Image...")
	for imgp in tqdm(image_list):
	    with open(Text_path + imgp[:-1*(len(Text_Extn))] + Text_Extn , "w") as file:
	        file.write(pytesseract.image_to_string(Image.open(Image_path + imgp)))

	print("Converted Image to Text")
