def run_main():
		inp1 =[1,3,4,5,7]
		inp2 = [2,4,6,7,8]
		solution = Solution()
		print(solution.intersect(inp1,inp2))
		print(soultion.data['1'])
		print(solution.union(inp1,inp2))

class Solution:
	def __init__(self,data):
		self.data = data
		
	def intersect(self,inp1,inp2):
		d = {}

		for elm in inp1: # o(n)
			if elm in d:
				d[elm] = d[elm] +1
			else:
				d[elm] = 1

		for elm in inp2: # o(m)
			if elm in d:
				d[elm] = d[elm] +1
			else:
				d[elm] = 1
		
		key_list = []
		unique_list = []

		for k,v in d.items(): # o(n+m)
			#k = None
			
			if v == 2:
				key_list.append(k)
			else:
				unique_list.append(k)

		union = unique_list + key_list
		print(union)
		return ",".join(str(i) for i in key_list)

	def union(self,inp1,inp2):
		pass



if __name__=="__main__":
	run_main()