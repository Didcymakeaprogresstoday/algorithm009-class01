class Solution:
	def findMin(self, nums: List[int]) -> int:
		if not nums:
			return
		if len(nums) == 1:
			return nums[0]
			
		if nums[0] < nums[-1]:
			return nums[0]

		l, r = 0, len(nums) - 1
		while l <= r:
			mid = l + (r - l) // 2
			if nums[mid] < nums[mid - 1]:
				return nums[mid]
			if nums[mid] > nums[mid + 1]:
				return nums[mid + 1]
			if nums[mid] > nums[0]:
				l = mid + 1
			else:
				r = mid - 1