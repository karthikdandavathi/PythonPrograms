class TreeNode:
	def __init__(self,data):
		self.left = None
		self.right = None
		self.value = data


class Solution:
	# @param root, a tree node
  # @return a list of lists of integers
	def level_order(self,root):
		solution =[]
		if root is None:
			return solution
		levelToProcess = [root]
		while len(levelToProcess)>0:
			numbersLevel = []
			nextLevel = []
			

