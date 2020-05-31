class Node:
	def __init__(self,val=None,children=None):
		self.val = val
		self.children = children

class Solution:
	#递归
	def preorder(self,root):
		if root is None:
			return []
		list = []
		list.append(root.val)
		if root.children:
			for item in root.children:
				list += self.preorder(item)