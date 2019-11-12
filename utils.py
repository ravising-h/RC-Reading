import re
import os
import difflib
import datetime

def Find_State(path):

	if not os.path.exists(path):
		raise AttributeError("{} path does not exists".format(path))
	
	with open("utils/State.txt","r") as file:
		list_of_states = file.read().split()


	with open(path,"r") as file:
		content = file.read()

	def similarity(word, pattern):
		return difflib.SequenceMatcher(a=word.lower(), b=pattern.lower()).ratio()

	for state in list_of_states:
		for word in content.split():
			if similarity(word,state ) > 0.83:
				return word.lower()

def Finding_Pattern(pattern, string):
	
	try:
		return re.search(pattern, string).group()
	except:
		return None

def Finding_Regs_No(string,pattern):

	slice_ = string.find(pattern[0:2])  + len(pattern[0:2])
	string = re.sub(r'[^\w]', ' ', string[slice_:])
	string = string[slice_:].replace(" ","")
	return Finding_Pattern(pattern,string)

def Finding_MFg_Date(string,pattern = r"[ :-]([0-9]){2}/([0-9]){4}" ):
	
	if Finding_Pattern(pattern, string) != None:
		return Finding_Pattern(pattern, string)[1:]

def Finding_Date(string,pattern = r"../../....|[0-9][0-9]-([A-Za-z]){3}-([0-9]){4}"):
	current_year = int(datetime.datetime.now().year)
	result = Finding_Pattern(pattern, string)
	if result is None:
		return None
	if int(result[-4:]) > current_year:
		years_back = - 15
		correction  = str(int(result[-4:]) + years_back)
		return result[:-4] + correction
	else:
		return result

def Finding_by_name(state,_path_):
    ele = "Name&Address".lower()
    ele1 = "owner's name".lower()
    ele2 = "name"
    with open(_path_,"r") as file:
        content = file.readlines()
    for i in range(len(content)-1):
        content[i] = content[i].lower().replace(" ","")
        if content[i].find(ele.lower()) != -1 or content[i].find(ele1.lower()) != -1 :
        	return content[i+1][:-1].replace(": ","")
    for i in range(len(content)):
    	content[i] = content[i].lower().replace(" ","")
    	value = content[i].find(ele2.lower()) 
    	if value != -1 :
        	if not("\n" in content[i][value + len(ele2):value + len(ele2) +4 ] ):
        		return content[i][value + len(ele2):-1].replace(": ","")
        	else:
        		return content[i+1][:-1].replace(": ","")

def Finding_CHNO(String,pattern):
	return  Finding_Pattern(pattern,String.replace(" ",""))

def Finding_Engine_no(string,pattern = r"[ \n][A-Z][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][0-9][0-9][0-9][ \n]|[ \n][A-Z][A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9][0-9][0-9][0-9][0-9][0-9][0-9][ \n]"):
	eng = ["engine no. ","e no.","eno.","Engine"]
	result = ""
	if Finding_Pattern(pattern,string):
		return re.sub(r'[^\w]', '',Finding_Pattern(pattern,string))
	