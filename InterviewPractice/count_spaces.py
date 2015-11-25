
def run_main():
	inp = "aaa bb cd"
	count_spaces()


def count_spaces():
	A = [4, 2, 7, 6, 8, 9, 1, 3, 2, 5, 6]
	B = [6, 3, 4, 1]

	Bdict = dict()

	for i in B:
		Bdict[i] = 0

	for j in A:
		if j in Bdict:
			Bdict[j] += 1

	Output = []

	for i in B:
		count = Bdict[i]
		for k in range(count):
			Output.append(i)

	A.sort()

	for j in A:
		if j not in Bdict:
			Output.append(j)
	print(Output)
	

if __name__=="__main__":
	run_main()
