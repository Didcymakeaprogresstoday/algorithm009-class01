class Solution:
	def twoSum(self,nums,target):
		dic = {}
		#也可以使用Collections.Count函数获得对应hashmap
		for i,v in enumerate(nums):
			dic[v] = i
		for i,v in div.items():
			if (target - v) in dic and dic[(target - v)] != i:
				return [i,dic[target - v]]