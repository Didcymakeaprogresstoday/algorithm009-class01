class Solution:
	def combine(self, n, k):
		if n <= 0 or k <= 0 or k > n:
			return []
		res = []
		self.dfs(1, k, n, [], res)
		return res

	def dfs(self, start, k, n, pre, res):
		#已找到的组合存储在pre中，从start开始搜索新的元素
		#当层数到k时，pre作为元素添加到res中
		if len(pre) == k:
			res.append(pre[:])
			return 

		for i in range(start, n + 1):
			pre.append(i)
			self.dfs(i + 1, k, n, pre, res)
			#回溯需要清理当前层，状态重置
			pre.pop()
