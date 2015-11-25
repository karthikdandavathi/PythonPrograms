import collections

def run_main():
	#inp = ["art","rat","bats","banana","stab","tar"]
	#oup = anagram_sort(inp)
	words = ["art","rat","bats","banana","stab","tar"]
	#print(oup)
	print(group_anagrams(words,count_letters_prehash))
\
def count_letters_prehash(word):
	return tuple(collections.Counter(word).items())

def group_anagrams(words,hash_function):
	result = {}

	for w in words:
		s = hash_function(w.lower())
		if s in result:
			result[s] = {w} 
		else:
			result[s] = {w} 
	return result.values()

if __name__=="__main__":
	run_main()