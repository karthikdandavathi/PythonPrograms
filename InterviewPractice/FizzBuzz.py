def run_main():
	fizz_buzz()

def fizz_buzz():

	for inp in range(1,100):

		if inp%3==0 and inp%5==0:
			print("fizzbuzz",end=",")

		elif inp%3==0:
			print("fizz",end=",")

		elif inp%5==0:
			print("buzz",end=",")

		else:
			print(inp,end=",")


if __name__=="__main__":
	run_main()