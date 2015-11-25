""""
	Fibonacci numbers are numbers that are 
	1,1,2,3,5,8
	i.e., if f(n) = f(n-1)+f(n-2) for n>2
"""

def run_main():
	print(F(6))

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

if __name__ == "__main__":
    run_main()