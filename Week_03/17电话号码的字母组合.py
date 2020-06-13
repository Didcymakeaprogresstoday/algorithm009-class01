class Solution:
	def letterCombinations(self, digits):
		res = []
		if not digits:
			return res
		phone_key = {
					'2':['a','b','c']
					'3':['d','e','f'],
					'4':['g','h','i'],
					'5':['j','k','l'],
					'6':['m','n','o'],
					'7':['p','q','r','s'],
					'8':['t','u','v'],
					'9':['w','x','y','z']
		}
		def backtrack(comba, nextdigit):
			if len(nextdigit) == 0:
				res.append(comba)
			else:
				for letter in phone_key[nextdigit[0]]:
					backtrack(comba + letter, nextdigit[1:])
		backtrack('',digits)
		return res			
