class Solution:
	def lemonadeChange(self, bills):
		five, ten = 0, 0
		for pay in bills:
			if pay == 5:
				five += 1
			elif pay == 10:
				ten += 1 
				five -= 1
			elif ten > 0:
				ten -= 1
				five -= 1
			else:
				five -= 3
			if five < 0:
				return False
		return True
