def run_main():
	input = [1,-1,4,3,9,11,7,7,1,9]
	print(check_unique_element_array(input))


def check_unique_element_array(input_arr):
	arr_set = set()
	print(input_arr)
	input_arr.sort()
	inp_dict = {}
	flag = 0
	unique_elements =[]
	

	for i in range (0,len(input_arr)):
		if input_arr[i] not in inp_dict:
			inp_dict[input_arr[i]] = flag
		else:
			inp_dict[input_arr[i]] = flag+1
		
	for k,v in inp_dict.items():
		if (v==0):
			unique_elements.append(k)
	return unique_elements
	
	#print("unique elements are: "+str(unique_elements))

if __name__=="__main__":
	run_main()