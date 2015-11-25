
def is_palindrome(input_str):
	input_list = list(input_str)
	j = len(input_list)

	for i in range(1,j):
		while (input_list):
			if input_list[1]==input_list[-1]:
				del input_list[-1]
				del input_list[1]
				return is_palindrome(input_list)
			else:
				print("not a palindrome")
				return False
			
def run_main():
	input = "redkkder"
	is_palindrome(input)

if __name__=="__main__":
	run_main()
