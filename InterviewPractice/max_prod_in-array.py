
#inp = [-1, -3, -4, 2, 0, -5]

import sys
def run_main():
	#\inp = [-1, -3, -4, 2, 0, -5]
	inp = [-10,-22,4,13]
	#inp = [10]
	#print(max(11,11))
	print(solution(inp))


def solution(inp):

	try:
		lenth = len(inp)
	except Exception:
		print("not valid input format")
		sys.exit()

	if lenth==0:
		print("no input")
		sys.exit()

	elif lenth==1:
		return inp[0]

	else:
		inp.sort()
		first_prod = inp[0]*inp[1]
		last_prod = inp[-1]*inp[-2]
		return max(first_prod,last_prod)

if __name__=="__main__":
	run_main()