def run_main():
	inp = [88, 105, 3, 2, 200, 0, 10]
	print_missing_elements(inp)

def print_missing_elements(inp):
	oup = []
	for i in range(0,99):
		if i not in inp:
			oup.append(i)
		else:
			pass
	start = 0
	end = 0
	

if __name__=="__main__":
	run_main()