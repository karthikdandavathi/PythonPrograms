def run_main():
   A = [1,5,2,1,4,0] 
   #A = [1,2,3,-3]
   print(solution(A))

# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    n = len(A)
    range_upper = [0]*n
    range_lower = [0]*n

    for index in range(n):
        range_upper[index] = index + A[index]
        range_lower[index] = index - A[index]
    range_upper.sort()
    range_lower.sort()
    
    range_lower_index = 0
    interesection_cnt =0
     
if __name__=="__main__":
    run_main()