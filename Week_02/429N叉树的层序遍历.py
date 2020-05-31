class Node:
    def __init__(self, val=None,children=None):
        self.val = val
        self.children = children

class Solution:
	def levelOrder(self, root: 'Node'):
		if root is None:
			return []
        queue = [root]                                          #初始化一个root
        res = []
        while queue:
            child = []                                          #该轮循环的结果集
            node = []                                           #为下一轮while循环提供新数据集
            for item in queue:                                  #因为是N叉树,所以需要遍历
                child.append(item.val)
                if item.children: node += item.children
            res.append(child)
            queue = node                                        #重要!  赋值给新 收集到的 子节点数据
        return res



