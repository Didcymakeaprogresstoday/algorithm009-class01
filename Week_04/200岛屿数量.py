class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if not grid:
			return 0
		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					self.dfs(grid, i, j)
					count += 1

	def dfs(self, grid, i, j):
		#将所有连在一起的 "1" 标记为"0"
		if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':#终止条件
			return
		grid[i][j] = '0'
		self.dfs(grid, i + 1, j)
		self.dfs(grid, i - 1, j)
		self.dfs(grid, i, j + 1)
		self.dfs(grid, i, j - 1)
