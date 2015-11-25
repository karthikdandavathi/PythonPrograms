def run_main():
	inp = [1,3,5,11,19]
	s = Solution()
	s.BST_level(3)

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(TreeNode):
	def BST_level(self,root):
		solution = []
		if root is None:
			return solution

		levelToProcess =[root]
		while(levelToProcess>0):
			numberslevel =[]
			nextlevel =[]

			for temp in levelToProcess:
				numberslevel.append(temp.val)

				if temp.left is not None:
					nextlevel.append(temp.left)
				if temp.right is not None:
					nextlevel.append(temp.right)
			solution.append(numberslevel)
			levelToProcess = nextlevel
		return solution