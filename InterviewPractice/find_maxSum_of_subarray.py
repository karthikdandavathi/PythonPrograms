def run_main():
	inp =[1,-3,5,2,-9,-8,-6,4,4]
	print(solution(inp))

def solution(inp):
	max_sum = 0
	arr_sum = 0

	for i in range(len(inp)):
		arr_sum = arr_sum+inp[i]
		if max_sum<arr_sum:
			max_sum = arr_sum
		elif arr_sum<0:
			arr_sum = 0
	return max_sum

if __name__=="__main__":
	run_main()