import math

def run_main():
    a =54
    b =3
    print(pow(a,b))

def pow(a, b):
  if b == 0:
    return 1
  elif b%2 == 0:
    c = pow(a, b/2)
    return c*c
  else:
    return a*pow(a, b-1)
	

	
    
if __name__=="__main__":
	run_main()