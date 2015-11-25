def run_main():
	inp1 = 'abcdbcad'
	inp1 = list(inp1)
	find_shortest_palindrome(inp1)

def find_shortest_palindrome(inp1):
	l = len(inp1)
	i =0
	count = l-1
	j = l-count
	
	while(i<l and j<l):
		if inp1[i]==inp1[j]:
			print("ok"+str(inp[i])+str(inp1[j]))

		elif inp1[i]!=inp1[j]:
			i = i+1
			j = j+1
		else:
			count = count-1
			

	





if __name__=="__main__":
	run_main()