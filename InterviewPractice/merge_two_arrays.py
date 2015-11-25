import sys
import os

def run_main():
	inp1 = [4,3,1,2,5]
	inp2 = [7,8,6,9]
	merge_two_arrays(inp1,inp2)

def merge_two_arrays(inp1,inp2):
	oup = []
	""""
	for i in range(0,len(inp1)-1):
		oup.append(i)

	for i in range(0,len(inp2)-1):
		oup.append(i)
	
	oup.sort()
	print(oup)
	"""
	


if __name__=="__main__":
	run_main()
