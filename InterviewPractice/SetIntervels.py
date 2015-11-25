import os
import sys

def run_main():
	inp = [12,20,2,6,5,10,9]
	set_intervels(inp)

def set_intervels(inp):
	inp.sort()
	output =[]
	n = ""

	for item in inp:
		if item+1 in inp:
			if item-1 in inp:
				pass
			else:
				n = str(item)+"-"
		else:
			if item-1 in inp:
				n = n+str(item)
				output.append(n)
			else:
				output.append(str(item))
	print (",".join(output))

if __name__=="__main__":
	run_main()