class Solution:
	def majorityElement(self, nums):
		# #使用collecitons模块
		# import collections
		# hashmap = collections.Counter(nums)
		# mx, mx_i = 0, 0
		# for i, v in hashmap.items():
		# 	if v > mx:
		# 		mx = v
		# 		mx_i = i
		# return mx_i

		#分治
		if not nums:
			return None
		if len(nums) == 1:
			return nums[0]
		a = self.majorityElement(nums[:len(nums) // 2])
		b = self.majorityElement(nums[len(nums) // 2:])
		if a == b:
			return a
		return [b,a][nums.count(a) > len(nums) // 2]