class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def buildTree(self, preorder, inorder):
		#递归终止条件
		if not preorder or not inorder:
			return 

		#先序遍历的第一个节点为根节点
		root = TreeNode(preorder[0])
		#中序遍历的根节点的左边为根的左子树
		index = inorder.index(preorder[0])
		#进行递归
		root.left = self.buildTree(preorder[1:1 + index], inorder[:index])
		root.right = self.buildTree(preorder[1 + index:], inorder[index + 1:])
		return root