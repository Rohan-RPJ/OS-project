import readinput

def fifo(page_list,frames_no):
	frames=[]
	hit=0
	attempts=len(page_list)
	for page in page_list:
		if page in frames:
			hit+=1
		else:
			if len(frames)==frames_no:
				frames.pop(0)
			frames.append(page)
	hr=float(hit)/attempts
	print("***"*4)
	print ("Frames:%d hits:%d Total attempts:%d Hit Ratio:%.2f "%(frames_no,hit,attempts, hr))

def lru(page_list, frames_no):
	frames=[]
	recent=[]
	hit=0
	attempts=len(page_list)
	
	for page in page_list:
		
		#Update the page to more recent location
		if page in recent:
			recent.remove(page)
			recent.append(page)
			print ("Page update to recent",page)
		else:
			if len(recent)==frames_no:
				old=recent.pop(0)
				print ("Popped from recent", old)
			recent.append(page)
			print ("Page added to recent",page)
		print ("recent:",recent)
		if page in frames:
			hit+=1
		else:
			if len(frames)<frames_no:
				frames.append(page)
			else:
				frames.remove(old)
				frames.append(page)
	hr=float(hit)/attempts
	print("***"*4)
	print ("Frames:%d hits:%d Total attempts:%d Hit Ratio:%.2f "%(frames_no,hit,attempts, hr))

def lfu(page_list, frames_no):
	frames=[]
	freq=[]
	hit=0
	tot=len(page_list)
	for page in page_list:
		if page not in frames:
			if len(frames)==frames_no:
				ind=freq.index(min(freq))
				poped=frames.pop(ind)
				freq.pop(ind)
				print ("%d was replaced"%(poped))
			frames.append(page)
			print ("Frames",frames)
			freq.append(0)
			print ("Freq",freq)
		else:
			
			freq[frames.index(page)]+=1
			hit+=1
	
	attempts=len(page_list)
	hr=float(hit)/attempts
	print("***"*4)
	print ("Frames:%d hits:%d Total attempts:%d Hit Ratio:%.2f "%(frames_no,hit,attempts, hr))


def getloc(elm,ind,lis):
	if elm not in lis:
		return -1
	else:
		return lis[ind+1:].index(elm)
				
def optimal(page_list,frames_no):
	frames=[]
	freq=[]
	hit=0
	tot=len(page_list)
	for page in page_list:
		if page not in frames:
			if len(frames)== frames_no:
				ind_list=[]
				for frame in frames:
					ind_list.append(getloc(frame,page_list.index(page),page_list))
				max_ind= ind_list.index(max(ind_list))
				poped=frames.pop(max_ind)	
				print ("%d was popped"%(poped))
				print ("Frames:",frames)	
			frames.append(page)
			print (page,"was added to the list")
			print ("Frames:",frames)
		else:
			hit+=1
			#print ("Hit")
	
	attempts=len(page_list)
	hr=float(hit)/attempts
	print("***"*4)
	print ("Frames:%d hits:%d Total attempts:%d Hit Ratio:%.2f "%(frames_no,hit,attempts, hr))
			
	
def main():
	print ("1. Read from DOCX")			
	print ("2. Read from XLSX")
	
	ch = int(input("Enter choice:"))
	ext=""
	if ch==1:
		ext="docx"
	elif ch==2:
		ext="xls"		
	
	page_list= readinput.getpagelist(ext)
	print ("page list:",page_list)
	
	print ("========FIFO======")
	fifo(page_list,3)
	print("***"*4)
	fifo(page_list,4)	
	print ("========LRU========")
	lru(page_list,3)
	print("***"*4)
	lru(page_list,4)
	print ("===========LFU=========")
	lfu(page_list,3)
	print("***"*4)
	lfu(page_list,4)
	print ("===========Optimal==============")
	optimal(page_list,3)
	print("***"*4)
	optimal(page_list,4)
	print("***"*4)

main()

