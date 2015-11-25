import sys
def run_main():
	#arr = [920]
	#dep = [930]
	arr = [900, 940, 950, 1100, 1500,1800]
	dep = [910, 1200, 1120, 1130, 1900, 2000]
	n = 6
	print(solution(arr,dep,n))

def solution(arr,dep,n):
	i=0
	j=0
	nop = 0
	mnop = 0
	loop = 0
	
	l = len(arr)
	h =  len(dep)

	if (not l ) or (not h) or (l and h !=n):
		print("bye1")
	elif l is 1 and h is 1 and arr[i]>=dep[j]:
		print ("bye")
	else:
		while(i<n and j<n):
			#print("looping "+str(loop) +" times")
			if (arr[i]<dep[j]):
				#print(mnop)
				i = i+1
				nop = nop+1
				if (nop>mnop):
					mnop = nop
			elif (arr[i]>dep[j]):
				j = j+1
				nop = nop-1
				#mnop_list.append(mnop)
				loop = loop+1
			else:
				print("arrival and departure cant be equal so crashing the program")
				sys.exit()
	return mnop


if __name__=="__main__":
	run_main()