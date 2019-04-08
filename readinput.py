'''
Script to read the input from respective files
'''
#from docx import Document
import xlrd
import os

def read_doc(file_path):
		doc= Document(file_path)
		fulltxt=[]
		for para in doc.paragraphs:
			fulltxt.append(para.text.strip())
		return fulltxt

'''
Returns a list containing page number from the file with extension file_ext
path= Location where MINI PORJECT INPUT FILES folder is
'''
def getpagelist(file_ext,path=None):
	dir_name= 'MINI PROJECT INPUT FILES'
	file_name='FIFO,OPTIMAL,LRU,LFU'
	if path==None: #Looks in the current folder if no path is provided
		path=os.getcwd()
	if '.' in file_ext: #trimming the '.' incase it is provided
		file_ext=file_ext[1:]

	pagefile_path=os.path.join(path,dir_name,file_name+"."+file_ext)
	#checking extension and calling appropriate read function
	if file_ext.startswith("docx"):
		pagefile_txt=read_doc(pagefile_path)
	elif file_ext.startswith("xlsx"):
		pass
	else:
		pagefile_txt=["0"]
	
	page_list=list(map(int,pagefile_txt[0].split("\t")))

	return page_list
	

def  read_xl(file_path):
	# give location of file
	loc = (file_path)
	
	# to open the workbook
	wb = xlrd.open_workbook(loc)
	sheet = wb.sheet_by_index(0)
	
	process_size = []
	blocks_size = []
	"""for row in range(sheet.nrows):
		# print (sheet.row_values(row))"""
	for size in sheet.row_values(0):
		if type(size) is float:
			process_size.append(int(size))
			
	for size in sheet.row_values(1):
		if type(size) is float:
			blocks_size.append(int(size))
	# print(process_size, blocks_size)
	return process_size, blocks_size
	










