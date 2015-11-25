import sys

def run_main():
	#inp = [1,3,5,3,7,8]
	#inp = [1,3,4]
	inp = [1,2,3,3,1,2,8]
	print(solution(inp))

def solution(inp):
	if not inp:
		sys.exit()
	elif len(inp)==1:
		return inp
	else:
		dcounter = {}

		for elm in inp:
			if elm in dcounter:
				dcounter[elm] = dcounter[elm] +1
			else:
				dcounter[elm] = 1

	for k,v in dcounter.items():
		if v==1:
			return k
	print("no such element")

if __name__=="__main__":
	run_main()