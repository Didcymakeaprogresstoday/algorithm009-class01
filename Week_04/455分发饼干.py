class Solution:
	def findContentChildren(self, g, s):
		#贪心算法
		g.sort()
		s.sort()
		if len(s) == 0 or len(g) == 0 or s[-1] < g[0]:
			return 0
		ans = i = j = 0
		while i < len(g) and j < len(s):
			if s[j] >= g[i]:
				ans += 1
				s[j] = 0
				i += 1
			j += 1
		return ans
