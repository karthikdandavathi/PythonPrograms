def run_main():
    input = [1,3,4,5,6,9]
    binary_search(input,9)

def binary_search(inp,number):
	l = len(inp)
	start = inp[0]
	last = inp[l-1]
	middle = (start+last)//2
	
	if(0<number<middle):
		binary_search(inp[:middle],number)
	elif(middle<number<last):
		binary_search(inp[middle:],number)
	elif(number==middle):
		print("number found: "+str(middle))

	print("number found: "+str(number))
	
if __name__=="__main__":
	run_main()
