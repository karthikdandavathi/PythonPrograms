"""
	Find K-th smallest element from the given array
"""
def run_main():
	inp = [44,12,55,10,9,8,99,11]
	p =0
	k =4
	print(find_k-th_smallest_element(inp,p,k))

def find_k-th_smallest_element(inp,p,k):
	"""
		pivot = inp[0]

		fromor elm in inp:
			if elm>p:

	"""
	for p in inp:
		if p==k:
			return inp[0]

		elif p<k:
			find_k-th_smallest_element(inp,p+1,len(inp))

		elif p>k:
			find_k-th_smallest_element(inp,0,p-1)	

def partition(inp,low,up):

	i = 0
	j = len(inp)

	key = inp[0]

	while(n>0):
			


if __name__=="__main__":
	run_main()