import os
import sys

def run_main():
	inp1 = [11,2,3,5]
	inp2 = [10,11,1,7,2]
	find_common_elements(inp1,inp2)

def find_common_elements(inp1,inp2):
	inp1.sort()
	inp2.sort()

	result = []
	
	for elm in inp1:
		if elm in inp2:
			result.append(elm)
	print (result)

	
if __name__=="__main__":
	run_main()