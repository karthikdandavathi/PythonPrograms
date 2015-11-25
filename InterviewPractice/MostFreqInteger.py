def run_main():
    input = [2,1,3,2,2,1]
    find_most_freq_integer(input)

def find_most_freq_integer(input_arr):
	count = dict()
	counter =0
	for i in input_arr:
		if i in count:
			count[i] += 1
			counter = counter+1
			print(str(i)+ " appeared : " + str(count[i]) +"times")	
		else:
			count[i]= 1
			counter =1
			print(str(i)+ " appeared : " + str(count[i]) +"times")	

	
    
if __name__=="__main__":
	run_main()
