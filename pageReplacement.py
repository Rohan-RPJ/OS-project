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
	print "hits:%d Total attempts:%d Hit Ratio:%.2f "%(hit,attempts, hr)

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
			print "Page update to recent",page
		else:
			if len(recent)==frames_no:
				old=recent.pop(0)
				print "Popped from recent", old
			recent.append(page)
			print "Page added to recent",page
		print "recent:",recent
		if page in frames:
			hit+=1
		else:
			if len(frames)<frames_no:
				frames.append(page)
			else:
				frames.remove(old)
				frames.append(page)
	hr=float(hit)/attempts
	print "hits:%d Total attempts:%d Hit Ratio:%.2f "%(hit,attempts, hr)
					

page_list=[1,3,0,3,5,6,3]
print "FIFO"
fifo(page_list,3)
fifo(page_list,4)	
print "LRU"
lru(page_list,3)
lru(page_list,4)
