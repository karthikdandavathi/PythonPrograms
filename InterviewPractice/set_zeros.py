from itertools import repeat

def run_main():
	row1 = [2,0,1]
	row2 =[2,1,1]
	row3 = [1,0,1]
	column1 = [1,1,1]
	column2 = [1,1,0]
	column3 = [1,1,2]
	rows = [row1,row2,row3]
	columns = [column1,column2,column3]

	set_zeros(rows,columns)

def make_zero(inp):
	l = len(inp)
	inp = []
	for i in range(0,l):
		inp.append(0)
	print(inp)
	return inp

def set_zeros(rows,columns):
	count = 0
	oup = []
	for i in range(0,len(rows)):
		for j in range(0,len(rows[i])):
			if rows[i][j]==0:
				make_zero(rows[i])
				oup.append(inp)
			else:
				inp = rows[i]
				oup.append(inp)
	print(rows[i])
	#print(count)

	for j in range(0,len(columns)):
		pass
		#print(columns[j])




if __name__=="__main__":
	run_main()