def run_main():
	inp = [5, 3, 5, 1, 3, 3]
	function(inp)

def function(inp):

	if len(inp)<=0:
		return False
	elif len(inp)<1:
		return inp

	else:
		dcounter = dict()
		oup = []
		oup.append(inp[0])
		j = 0

		for i in range(1,len(inp)):
			if oup[j] in inp:
				dcounter[oup[j]] = dcounter[oup[j]]+1
			else:
				dcounter[oup[j]] = 1
		print(dcounter)
		print(oup)
if __name__=="__main__":
	run_main()