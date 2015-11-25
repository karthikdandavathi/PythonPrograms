from collections import Counter
def run_main():
	inp = [3,5,7,15,1]
	array_pair(inp,16)


def array_pair(inp,k):
	if len(inp)<2:
		return
	dcounter = {}
	count = 0
	seen = set()
	for elm in inp:
		if elm in dcounter:
			dcounter[elm]= dcounter[elm]+1
		else:
			dcounter[elm]=1

	for elm in inp:
		target = k- elm
		if target in inp:
			if target not in seen:
				seen.add(target)
				while(dcounter[target]>0):
					dcounter[target] = dcounter[target]-1
				print(str(elm)+' and '+str(target)+' are pairs ')

if __name__=="__main__":
	run_main()