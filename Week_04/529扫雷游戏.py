class Solution:
	def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
		if not board:
			return []

		m, n = len(board), len(board[0])
		i, j = click[0], click[1]

		if board[i][j] == "M":
			board[i][j] == "X"
			return board

		self.dfs(board, i, j)
		return board

	def dfs(self, board, i, j):
		if board[i][j] != 'E':
			return 

		m, n = len(board), len(board[0])
		directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)]

		mine_count = 0
		for d in directions:
			n_i, n_j = i + d[0], j + d[1]
			if 0 <= n_i < m and 0 <= n_j < n and board[n_i][n_j] == "M":
				mine_count += 1

		if mine_count == 0:
			board[i][j] = 'B'
		else:
			board[i][j] = str(mine_count)
			return

		for d in directions:
			n_i, n_j = i + d[0], j + d[1]
			if 0 <= n_i < m and 0 <= n_j < n:
				self.dfs(board, n_i, n_j)

