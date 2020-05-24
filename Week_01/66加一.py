#第一次尝试
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
         #将数组转化成整数
        n = len(digits)
        post_digits = []
        num = 0
        for i in range(n):
             num += digits[i]*pow(10,n-i-1)
        num += 1
        #将整数转化成数组
        num_str = str(num)
        for i in num_str:
            post_digits.append(int(i))
        return post_digits

