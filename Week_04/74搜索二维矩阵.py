class Solution:
	def searchMatrix(self, maxtrix: List[List[int]], target: int) -> bool:
		# #O(m * n)空间复杂度 max(O(m),O(log(m*n)))时间复杂度
		# if not maxtrix:
		# 	return False
		# m, n = len(maxtrix), len(maxtrix[0])
		# l, r = 0, m * n - 1
		# ls = []
		# for i in range(m):
		# 	ls += maxtrix[i]

		# print(ls)

		# while l <= r:
		# 	mid = (l + r) // 2
		# 	if ls[mid] == target:
		# 		return True
		# 	elif ls[mid] > target:
		# 		r = mid - 1
		# 	else:
		# 		l = mid + 1
		# return False

		#O(1)空间复杂度 O(log(m*n))时间复杂度
		if not maxtrix:
			return False
		m, n = len(maxtrix), len(maxtrix[0])
		l, r = 0, m * n - 1
		while l <= r:
			mid = (l + r) // 2
			# a, b 表示mid当前所在matrix中的位置
			a, b = divmod(mid, n)
			print(a,b)
			if maxtrix[a][b] == target:
				return True
			elif maxtrix[a][b] > target:
				r = mid - 1
			else:
				l = mid + 1
		return False
