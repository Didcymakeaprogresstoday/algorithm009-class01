class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.fight = None

class Solution:
	def lowestCommonAncestor(self,root:'TreeNode',p:'TreeNode',q:'TreeNode'):
		#终止条件
		if not root or root == p or root == q:
			return root
		#递推
		left = self.lowestCommonAncestor(root.left, p, q)
		right = self.lowestCommonAncestor(root.right, p, q)

		if not left and not right:
			return 
		if not left:
			return right
		if not right:
			return left
		return root