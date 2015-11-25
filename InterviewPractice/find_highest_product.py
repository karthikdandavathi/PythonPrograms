
def run_main():
	inp = [0,-1,2,2,-7,10,2]
	find_highest_product(inp)

def find_highest_product(inp):
	inter_list = []
	count = 0
	count2 =0
	prod = 0
	oup = []
	for i in range(0,len(inp)):
		while(count<3):
			count = count+1
			inter_list.append(max(inp))
			inp.remove(max(inp))
	for j in range(0,len(inp)):
		while(count2<2):
			count2 = count2+1
			inter_list.append(min(inp))
			inp.remove(min(inp))

	
	prod1 = inter_list[0]*inter_list[1]*inter_list[2]
	prod2= inter_list[0]*inter_list[1]*inter_list[-1]
	prod3 = inter_list[0]*inter_list[-1]*inter_list[-2]
	oup.append(prod1)
	oup.append(prod2)
	oup.append(prod3)
	print(oup)
	print(max(oup))


if __name__=="__main__":
	run_main()