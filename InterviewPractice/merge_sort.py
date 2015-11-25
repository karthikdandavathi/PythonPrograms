import os
import sys

def run_main():
	inp = [3,2,1,5,6,2,1,22,2,1,4,15,699999,7,4,2,4,77]
	print (merge_sort(inp))

def merge_sort(inp):
	if len(inp)<=1:
		return inp

	l = len(inp)
	m = l//2

	left = merge_sort(inp[:m])
	right = merge_sort(inp[m:])

	return merge(left,right)

def merge(left,right):
	if not left:
		return right
	if not right:
		return left

	if left[0]<right[0]:
		return [left[0]]+ merge(left[1:],right)
	return [right[0]]+ merge(left,right[1:])

if __name__=="__main__":
	run_main()