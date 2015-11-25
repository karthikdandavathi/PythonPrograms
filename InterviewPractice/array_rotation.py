

def run_main():
	inp1 = [1,3,2,4,5]
	inp2 = [4,5,1,3,2]
	check_array_rotation(inp1,inp2)

def check_array_rotation(inp1,inp2):
	index = 0
	index_dict_inp1 = {}
	index_dict_inp2 = {}
	l1 = len(inp1)
	l2 = len(inp2)
	#for i in range(0,len(inp1)):
		#index_dict_inp1[i]=inp1[i]

	#for j in range(0,len(inp2)):
		#index_dict_inp2[j]=inp2[j]
	n = 0
	j = 0
	for i in range(0,l1):
		if n>l1:
			n = 0
		elif n<l1:
			if inp2[i]==inp1[j]:
				n = i
				j = j+1
	print()

	#print(index_dict_inp1)
	#print(index_dict_inp2)


if __name__=="__main__":
	run_main()