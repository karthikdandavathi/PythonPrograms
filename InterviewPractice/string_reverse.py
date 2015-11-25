def run_main():
	s = "dandavathi sai karthik"
	print(function(s))

def function(s):
	s = s.replace(" ","")
	#print(s)
	if len(s)<=0:
		return False
	elif 0<len(s)<1:
		return s
	else:
		r = ""
		for c in s:
			r = c+r
		return r

if __name__=="__main__":
	run_main()