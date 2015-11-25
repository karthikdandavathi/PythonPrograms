
def run_main():
	inp_str = "san jose state university"
	#inp_str =""
	print(find_first_non_repeated_character(inp_str))


def find_first_non_repeated_character(inp):
	inp = inp.replace(" ","")

	if len(inp)<=0:
		print("string is empty")

	elif 0<len(inp)<1:
		return inp

	else:
		index =0
		dcounter = {}
		for char in inp:
			if char in dcounter:
				dcounter[char] = dcounter[char]+1
			else:
				dcounter[char] = 1

		first_index = None
		for k,v in dcounter.items():
			if (v==1 and first_index is None):
				first_index = inp.index(k)
			elif(v==1 and first_index is not None):
				next_index = inp.index(k)
				if next_index < first_index:
					first_index = next_index
				else:
					pass
		return inp[first_index]



if __name__=="__main__":
	run_main()