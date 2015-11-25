def run_main():
	inp = [10,15,22,5]
	k = 25

	print(find_sum(inp,k))

def find_sum(inp,k):
	d = {}
	for elm in inp:
		d[elm] = elm
	for elm in inp:
		target = k-elm
		if target in d:
			return (target,elm)
		else:
			pass

"""
array is sorted
1) two i = 0, j = len(inp)
 for i in range(len(inp))
2) if inpi+j = k , then i,j are pairs
3) elifif i+j < k , i= i+1
4) else j = j+1
5) else print no pairs found


def find_sum(inp,k):
	a = 0
	b = len()
	for i in range(len(inp)):
		for j in range()

"""
if __name__=="__main__":
	run_main()