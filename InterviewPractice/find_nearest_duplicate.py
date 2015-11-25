def run_main():
	inp = [1,2,11,12]
	k = 2

	print(function(inp,k))

def function(inp,k):
	isDuplicateFound = False

	for i in range(0,len(inp)):
		for j in range(k,len(inp)):
			if inp[i]==inp[j]:
				isDuplicateFound = True
				return isDuplicateFound
			else:
				return isDuplicateFound 
			
if __name__=="__main__":
	run_main()
