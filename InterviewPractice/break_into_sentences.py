
def run_main():
	inp = 'The predicate is the part that provides the action and additional information. The verb is the main part of a predicate, so the predicate could be a single verb like stands, puffs, or plows.'
	break_into_sentences(inp)

def break_into_sentences(inp):
	interim_str = inp.split('.')
	
	oup = list(interim_str)
	l = len(oup)
	print(oup[:l-1])


if __name__=="__main__":
	run_main()