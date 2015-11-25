def run_main():
	#inp = [1,1,1,0]
	inp =  [1, 2, 3, -4, -1, 4]
	function(inp)

def function(inp):
	llist = []
	rlist = []
	ilist = []
	oup = []

	for i in range(len(inp)):
		if inp[i]<0:
			llist.append(inp[i])
		elif inp[i]>=0:
			rlist.append(inp[i])
		else:
			pass

	ilist = llist+rlist

	print(ilist)
	


if __name__=="__main__":
	run_main()