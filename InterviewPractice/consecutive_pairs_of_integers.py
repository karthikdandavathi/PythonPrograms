def run_main():
	inp = [1,3,3,2,1,2,6,5,4]
	print(solution(inp))

def solution(inp):

	inp.sort()
	dcounter = {}
	count = 0

	for elm in inp:
		if elm in dcounter:
			dcounter[elm] = dcounter[elm]+1
		else:
			dcounter[elm] = 1
	#print(dcounter)
	for k,v in dcounter.items():
		if v>=2:
			count = count + 1
		else:
			pass
	if (count==4):
		return True


if __name__=="__main__":
	run_main()