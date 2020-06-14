class Solution:
	def jump(self, nums: List[int]) -> int:
		n = len(nums)
		max_, end, step = 0, 0, 0
		for i in range(n - 1):
			if max_ >= i:
				max_ = max(max_, i + nums[i])
				if i == end:
					end = max_
					step += 1
		return step