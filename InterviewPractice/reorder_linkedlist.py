def run_main():
	sol = Solution()
	A = [100,200,3,4,1,2,5]
	sol.find_longest_cons_seq(A)

class Solution:
	# inp is a list
	# output should return consequtive list
	# o(n) time
	def find_longest_cons_seq(self,num):
		
		starttoend = {}
		endtostart = {}
		longest = 0
		min_num = 2147483647
		
		for i in range(0, len(num)):
    	start = num[i]
    	end = num[i]
    	if num[i] in startToEnd:
      	for i in range(0, len(num)):
      		start = num[i]
            end = num[i]
            if num[i] in startToEnd:
                end = startToEnd[num[i]]
                del startToEnd[num[i]]
                del endToStart[end]
            if num[i] in endToStart:
                start = endToStart[num[i]]
                del startToEnd[start]
                del endToStart[num[i]]
            if num[i]-1 in endToStart:
                start = min(start, endToStart[num[i]-1])
                del startToEnd[endToStart[num[i]-1]]
                del endToStart[num[i]-1]
            if num[i]+1 in startToEnd:
                end = max(end, startToEnd[num[i]+1])
                del endToStart[startToEnd[num[i]+1]]
                del startToEnd[num[i]+1]
            startToEnd[start] = end
            endToStart[end] = start
            longest = max(longest, end-start+1)
        return longest
	


if __name__=="__main__":
	run_main()



