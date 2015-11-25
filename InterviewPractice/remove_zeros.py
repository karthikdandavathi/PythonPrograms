import os
import sys

def run_main():
	inp = [12,3,1,0,6,0,7,0,2]
	remove_zeros(inp)

def remove_zeros(inp):
	l = len(inp)
	oup = list()
	count =0
	for i in range(0,l-1):
		if not (inp[i]^0 is 0):
			oup.append(inp[i])
		else:
			count+=1
	print (count)
	i =0
	while(i<count):
		oup.append(0)
		i = i+1
	print (oup)

if __name__=="__main__":
	run_main()