import os
import sys

def run_main():
	str_inp ="abcdefmmnopqrstuu"
	find_longest_sub_string(str_inp)

""""
when u iterate through the list you need to maintain the count of 
the unique characters as well 
"""
def find_longest_sub_string(str_inp):
	prev_char = None
	counter = []
	sequence = []
	count = 0
	for char in str_inp:
		if (char != prev_char):
			#print("entering ")
			start_char = char	
			count =count+1
		else:
			sequenc = start_char+'-'+prev_char
			counter.append(count)
			count = 0
	#print(counter)
	print(sequenc)
	print(max(counter))



if __name__=="__main__":
	run_main()