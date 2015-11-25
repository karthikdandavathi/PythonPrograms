import sys

def run_main():
	inp = [1,6,4,10,2]
	function(inp)

def function(inp):
	"""
	try:
		assertisnotainstanceof(inp,list)
	except Exception:
		print("exception")
		sys.exit()
	"""
	if len(inp)<=0:
		print("false")
	elif len(inp)<1:
		return inp

	else:
		oup = []
		l = len(inp)
		"""
"		for j in range(len(inp)):
			oup.append(inp[j])
			l = l-1
		"""
		for i in range(0,len(inp)-1):
			if not oup:
				oup.append("-")
			elif inp[i]<=oup.pop():
				oup.pop()
			else:
				print(oup.pop())
			
			oup.append(inp[i])

if __name__=="__main__":
	run_main()