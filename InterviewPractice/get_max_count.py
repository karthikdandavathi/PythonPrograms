
def run_main():
	inp = [2,1,-1,1,2,3,4,5,6,-1,1,2,3,4,5]
	get_max_count(inp)

def get_max_count(inp):
	counter =[]
	count =0
	l = len(inp)
	for i in range(0,l-1):
		if (inp[i]*i)>0:
			count+=1
		else:
			counter.append(count)
			count =0
			pass
	#print(counter)
	max_count = max(counter)
	print(max_count)

if __name__=="__main__":
	run_main()