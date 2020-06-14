class Solution:
	def canJump(self, nums: List[int]) -> bool:
		j_max, n = 0, len(nums)
		for i in range(n):
			if i <= j_max:
				j_max = max(j_max, i + nums[i])
			if j_max >= n - 1:return True
		return False