def run_main():
	inp = [2,1,12,11,22,33,13]
	print(quick_sort(inp))

def quick_sort(inp):
	less =[]
	equal = []
	greater = []

	if len(inp)>1:
		pivot = inp[0]
		for elm in inp:
			if elm < pivot:
				less.append(elm)
			if elm == pivot:
				equal.append(pivot)
			if elm > pivot:
				greater.append(pivot)
		return quick_sort(less)+equal+quick_sort(greater)
	else:
		return inp

if __name__=="__main__":
	run_main()