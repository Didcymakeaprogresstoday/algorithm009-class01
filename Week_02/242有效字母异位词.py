#hashmap
class Solution:
	def isAnagram(self,s,t):	
		dic = {}
		for i in s:
			dic[i] = dic.get(i,0) + 1
		for i in t:
			dic[i] = dic.get(i,0) - 1
		for i in dic.values():
			if i != 0:
				return False
		return True