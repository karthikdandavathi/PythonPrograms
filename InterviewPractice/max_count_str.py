
import sys
import os

def run_main():
	inp_str ="sai karthik dandavathi"
	#inp_str = 
	oup =get_max_count(inp_str)
	if oup is not None:
		print (oup)
	
def get_max_count(inp_str):

	try:
		inp_str = inp_str.replace(" ","")
	except Exception:
		print("inp string is not in expected data type")
		sys.exit()

	if len(inp_str)<=0:
		print('inp string is Null')

	elif 0<len(inp_str)<1:
		return inp_str

	else:
		dcounter = {}
		for char in inp_str:
			if char in dcounter:
				dcounter[char]=dcounter[char]+1
			else:
				dcounter[char]=1
	
		max_value = 0
		oup_key = None

		for k,v in dcounter.items():
			if v>max_value:
				max_value = v
				oup_key = k
		return oup_key,max_value

if __name__=="__main__":
	run_main()

# test cases for this code
""""
	1. null string: print message
	2. not a string: exception ..exit the program
	3. normal string - return output
"""