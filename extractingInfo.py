import os
import pandas as pd 
import numpy as np 
from utils import *
from ExtractingFromGoogleVisionOCR import GoogleOCR
from ExtractingFromTesseract import Tesseract
from tqdm import tqdm
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("API",help="Type g for Google API t for tesseract")
parser.add_argument("Path_Of_Images")
parser.add_argument("Path_Of_text")
args = parser.parse_args()
if args.API == "t":
	Tesseract(args.Path_Of_Images,args.Path_Of_text)
elif args.API == "g":
	GoogleOCR(args.Path_Of_Images,args.Path_Of_text)
else:
	raise ModuleNotFoundError("Wrong Choice: Choose either T for Tesseract or g for GoogleOCR")
Total_files = len(os.listdir(args.Path_Of_Images))
Total_Coloumns = 7
dataset = np.empty((Total_files,Total_Coloumns),dtype = object)
pattern = r"DL......."
with tqdm(total = len(os.listdir(args.Path_Of_text)) ) as pgr:
	for i,text_file in tqdm(enumerate(os.listdir(args.Path_Of_text))):

		_path_ =  args.Path_Of_text + "/" + text_file
		if not os.path.exists(_path_):
			raise AttributeError("{} path does not exists".format(_path_))
		with open(_path_,"r") as file:
			content = file.read()
		state_of_cust = Find_State(_path_)
		mapping_dict = json.loads(open("utils/RegNo.json","r").read())
		for key in list(mapping_dict.keys()):
			if state_of_cust == key:
				pattern =  mapping_dict[key]
				break
		dataset[i,0] = text_file
		dataset[i,1] = Finding_by_name(state_of_cust,_path_)
		dataset[i,2] = Finding_Regs_No(content,pattern)
		dataset[i,3] = Finding_CHNO(content,pattern= open("utils/Chasis.txt" ,"r").read())
		dataset[i,4] = Finding_Engine_no(content, pattern = open("utils/EngineNo.txt","r").read())
		dataset[i,5] = Finding_Date(content)
		dataset[i,6] = Finding_MFg_Date(content)
		pgr.update(1)
pd.DataFrame(dataset).to_csv("result.csv",index=False, header = ["Path","Owner's Name","Registration Number","Chasis Number","Engine Number","Registration Date","Date of Manufracture"])