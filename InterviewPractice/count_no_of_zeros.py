
def run_main():
	inp = 5
	print(solution(inp))

def factorsoffive(inp):
	count = 0
	while ((inp%5)==0):
		count = count+1
		inp = inp/5
	return count

def solution(inp):
	count =0
	for i in range(2,inp):
		count = count+factorsoffive(i)
	return count

if __name__=="__main__":
	run_main()