import sys

def run_main():
	inp = "aabbbcccc"
	print(solution(inp))

def solution(inp):

	if not inp:
		sys.exit()

	elif len(inp)==1:
		return inp+"1"
	else:
		prev_char = inp[0]
		count = 1
		out = []
		for char in inp[1:]:
			if char is not prev_char:
				out.append(prev_char)
				out.append(count)
				prev_char = char
				count = 1
			else:
				count = count+1
		out.append(char)
		out.append(count)
		return "".join(str(e) for e in out)

if __name__=="__main__":
	run_main()