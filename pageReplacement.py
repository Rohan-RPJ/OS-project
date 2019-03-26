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
	
page_list=[1,3,0,3,5,6,3]
fifo(page_list,3)
fifo(page_list,4)	
