def run_main():
	n = 3
	k = 5
	inp = "karthik"
	print(len(permute(inp)))

def permute(inp):
	result = []

	if len(inp)==1:
		result = [inp]
	else:
		for i,c in enumerate(inp):
			for perm in permute(inp[:i]+inp[i+1:]):
				result +=[c+perm]
	return result 



if __name__=="__main__":
	run_main()