""""
inp = ["art","rat","bats","banana","stab","tar"]
oup = [["art","rat","tar"],["bats","stab"],["banana"]]
"""
from collections import defaultdict

def run_main():
	inp = ["art","rat","bats","banana","stab","tar"]
	anagram_sort(inp)

def anagram_sort(inp):
	#inp.sort()
	d = defaultdict(list)
	for word in inp:
		d[''.join(sorted(word))].append(word)

	#print(d)
	print(sorted(d.values()))
	#print(d.values())
	

if __name__=="__main__":
	run_main()