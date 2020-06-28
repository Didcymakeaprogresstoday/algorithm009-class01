from typing import List
class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:
		if not grid:
			return 
		dp = grid 
		n, m = len(grid), len(grid[0])
		dp[n-1] += [0]
		for i in range(n-1, -1, -1):
			for j in range(m-1, -1, -1):
				if i == n-1:
					dp[i][j] += dp[i][j+1]
				elif j != m-1:
					dp[i][j] += min(dp[i][j+1], dp[i+1][j])
				else:
					dp[i][j] += dp[i+1][j]
		return dp[0][0] 

        # ##优化空间复杂度
        # n, m = len(grid), len(grid[0])
        # dp = grid[n-1] + [0]
        # for i in range(n-1, -1, -1):
        #     for j in range(m-1, -1, -1):
        #         if i == n-1:
        #             dp[j] += dp[j+1]
        #         elif j != m-1:
        #             dp[j] = min(dp[j], dp[j+1]) + grid[i][j]
        #         else:
        #             dp[j] += grid[i][j]
        # return dp[0]