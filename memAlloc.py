import readinput

def display(process_alloc, process_size):
	print("Process No.\tProcess Size\tBlock No.\n")
	for p in range(len(process_alloc)):
		if process_alloc[p] != -1:
			print(p+1,"\t\t",process_size[p],"\t\t",process_alloc[p],"\n")
		else:
			print(p+1,"\t\t",process_size[p],"\t\tNot allocated\n")


def firstfit(process_size, blocks_size):
	process_alloc = []
	for process in range(len(process_size)):
		for block in range(len(blocks_size)):
			if process_size[process] <= blocks_size[block]:
				process_alloc.append(block+1)	
				blocks_size[block] -= process_size[process]
				break
		if process+1 > len(process_alloc):
			process_alloc.append(-1)
	# print(process_alloc)	
	print("====FirstFit====")
	display(process_alloc, process_size)
	
	
def nextfit(process_size, blocks_size):
	process_alloc = []
	process = 0
	blk_no = len(blocks_size)-1
	while process < len(process_size):
		for block in range(len(blocks_size)):
				
			if process == len(process_size):
				break
				
			#print(process_size[process],blocks_size[block])
			if process_size[process] <= blocks_size[block]:
				process_alloc.append(block+1)	
				blocks_size[block] -= process_size[process]
				process += 1
				blk_no = block
				continue
				
			if block == blk_no:
				print("Not allocated\n")
				process_alloc.append(-1)
				process += 1
				
	# print(process_alloc)	
	print("====NextFit====")
	display(process_alloc, process_size)
	
	
def bestfit(process_size, blocks_size):
	process_alloc = []
	min_blk_size = -1
	pos = -1
	for process in range(len(process_size)):
		for block in range(len(blocks_size)):
			if process_size[process] <= blocks_size[block]:
				if min_blk_size is -1 or min_blk_size > blocks_size[block]:
					min_blk_size = blocks_size[block]
					pos = block 
		
		if min_blk_size is -1:
			process_alloc.append(-1)
		else:
			process_alloc.append(pos+1)	
			blocks_size[pos] -= process_size[process]
			min_blk_size = -1
			
	# print(process_alloc)	
	print("====BestFit====")
	display(process_alloc, process_size)
	
	
def worstfit(process_size, blocks_size):
	process_alloc = []
	max_blk_size = -1
	pos = -1
	for process in range(len(process_size)):
		for block in range(len(blocks_size)):
			if process_size[process] <= blocks_size[block]:
				if max_blk_size is -1 or max_blk_size < blocks_size[block]:
					max_blk_size = blocks_size[block]
					pos = block 
		
		if max_blk_size is -1:
			process_alloc.append(-1)
		else:
			process_alloc.append(pos+1)	
			blocks_size[pos] -= process_size[process]
			max_blk_size = -1
			
	# print(process_alloc)	
	print("====WorstFit====")
	display(process_alloc, process_size)
	
	
def main():
	process_size, blocks_size = readinput.read_xl("MINI PROJECT INPUT FILES/memory allocation startegies.xls")
	print(process_size,blocks_size)
	
	p_size, blks_size = process_size.copy(), blocks_size.copy()
	firstfit(p_size, blks_size)
	
	print(process_size,blocks_size)
	p_size, blks_size = process_size.copy(), blocks_size.copy()
	nextfit(p_size, blks_size)


	print(process_size,blocks_size)
	p_size, blks_size = process_size.copy(), blocks_size.copy()
	bestfit(p_size, blks_size)
	
	
	print(process_size,blocks_size)
	p_size, blks_size = process_size.copy(), blocks_size.copy()
	worstfit(p_size, blks_size)
main()
