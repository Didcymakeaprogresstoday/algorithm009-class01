class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	def inorderTraversal(self,root:TreeNode):
		stack,res = [root],[]
		while stack:
			i = stack.pop()
			if isinstance(i,TreeNode):
				stack.extend([i.right,i.val,i.left])
			elif isinstance(i,int):
				res.append(i)
		return res	