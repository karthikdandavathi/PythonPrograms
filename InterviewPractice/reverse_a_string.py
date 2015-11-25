def run_main():
	str_inp = "karthik"
	print(reverse_a_string(str_inp))

def reverse_a_string(str_inp):
	l = len(str_inp)
	if l<=1:
		return str_inp
	return reverse_a_string(str_inp[1:])+str_inp[0]


if __name__=="__main__":
	run_main()

