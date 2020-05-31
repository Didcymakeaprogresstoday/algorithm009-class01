class Solution:
	def groupAnagrams(self,strs):
		res = {}
		for item in strs:
			res[tuple(sorted(item))].append(item)#元组作为键 列表作为值
		return list(res.values())