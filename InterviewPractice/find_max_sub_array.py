""""
	Given an array, write a fn. to identify sub-array with max sum:

	inp =[1,-3,5,-2,9,-8,-6,4]
	oup = [5,-2,9]
	
"""
def run_main():
	inp =[1,-3,5,-2,9,-8,-6,4]
	find_max_sub_array(inp)


def find_max_sub_array(inp):
	arr_sum = 0
	max_sum = 0 
	cur_start = 0
	cur_end = 0
	start = 0
	end = 0

	for i in range(len(inp)):
		arr_sum = arr_sum + inp[i]
		#max_sum = arr_sum

		if arr_sum<0:
			cur_start = i+1
			arr_sum = 0

		elif arr_sum>max_sum:
			cur_end = i
			max_sum = arr_sum

		if cur_end>=cur_start:
			start = cur_start
			end = cur_end

	print("[",end="")
	for i in range(start,end):
		print(inp[i],end=",")
	print(inp[end],end="]\n")

	""""

		"""
if __name__=="__main__":
	run_main()