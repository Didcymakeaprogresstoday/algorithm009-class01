class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	def preorderTraversal(self,root:TreeNode):
		if root is None:
			return []
		stack,res = [root],[]

		#根左右
		while  stack:
			i = stack.pop()
			if i is not None:
				res.append(i.val)
				if i.right is not None:
					stack.append(i.right)
				if i.left is not None:
					stack.append(i.left)
		return res