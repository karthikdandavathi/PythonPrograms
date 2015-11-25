def run_main():
	print(function(61,-10))

def function(num,k):

	num = abs(num)
	k = abs(k)

	r = num%k
	q = int(num/k)
	out = []
	
	for i in range(1,k):
		out.append(q)
	for j in range(0,r):
		out[j] = out[j]+1

	return out

if __name__=="__main__":
	run_main()