def run_main():

	inp ="110011"
	print(function(inp))

def function(inp):

	count = 0
	inp = list(inp)
	
	for i in range(len(inp)):
		if inp[i]=='1':
			count = count+1

	return int(count*((count-1)/2))

if __name__=="__main__":
	run_main()