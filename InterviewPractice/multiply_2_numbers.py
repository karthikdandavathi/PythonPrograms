def run_main():
	multiply_2_numbers(7,10)

def multiply_2_numbers(a,b):
	prod = 0
	for i in range(min(a,b)):
		prod = prod+max(a,b)
	print(prod)
		



if __name__=="__main__":
	run_main()