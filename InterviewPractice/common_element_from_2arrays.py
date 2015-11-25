"""
Find the common elements of 2 int arrays
"""
import hashlib

def find_common_elements(first_arr,second_arr):
	hash_first_dict = dict()
	hash_second_dict = dict()
	
	hash_first_dict[hash(first_arr)]
	print(hash_first_dict.items())
	for elm in second_arr:
		hash_second_dict[hash(elm)] =elm

	combined_hash_dict = hash_first_dict.copy()
	combined_hash_dict.update(hash_second_dict)

	for k1,k2 in zip(hash_first_dict.keys(),hash_second_dict.keys()):
		
			#print(k1)
			print (hash_first_dict.get(k1))

def run_main():
	input1 = [1,4,3]
	input2 = [1,2,3]
	find_common_elements(input1,input2)

if __name__=="__main__":
	run_main()