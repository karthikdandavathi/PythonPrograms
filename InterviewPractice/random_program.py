def run_main():
	inp = "aabbcccd"
	sol = Solution()
	sol.function(inp)

class Solution:

	def __init__(self):
		pass

	def function(self,inp):
		prev_char = inp[0]
		count = 1
		oup = ""
		#print(prev_char)
		for char in inp[1:]:
			if char is prev_char:
				count = count+1
			else:
				prev_char = char
				oup = oup+prev_char+str(count)
				count = 1
		print(oup)
		
if __name__=="__main__":
	run_main()