import sys

def run_main():
	#inp = {1}
	inp = [1,2,2,3,4,4,4,4]
	test = Test()
	test.find_duplicate(inp)

class Test:
	def find_duplicate(self,inp):

		l = len(inp)

		if l<=0:
			print("empty list")

		elif 0<l<1:
			return inp

		else:
			dcounter = {}

			for elm in inp:
				if elm in dcounter:
					dcounter[elm] = dcounter[elm]+1
				else:
					dcounter[elm] = 1
			print(dcounter)
			run = 0
			for key,value in dcounter.items():
				run = run+1
				if value==2:
					print(key)
			print ("no of times this ran is: "+str(run))

if __name__=="__main__":
	run_main()