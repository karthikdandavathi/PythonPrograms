import sys
import os

def run_main():
	inp = [1,-1,-3,-4,-4,-3,7]
	find_duplicates(inp)

def find_duplicates(inp):
	unique_list = list()

	for elm in inp:
		if elm not in unique_list:
			unique_list.append(elm)
		else:
			print("duplicate found: "+str(elm))
	print(unique_list)

if __name__=="__main__":
	run_main()