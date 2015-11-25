def run_main():
	inp = [0,1,0,1]
	print(function(inp))

def function(inp):
	totalZeros = 0
	count = 0
	l = len(inp)

	for i in range(l):
		if inp[i]==0:
			totalZeros = totalZeros+1
			#print(totalZeros)
		elif inp[i]==1:
			count = count+totalZeros
			#print(count)
	return count	

if __name__=="__main__":
	run_main()
