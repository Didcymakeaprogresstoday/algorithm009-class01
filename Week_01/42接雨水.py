#双指针  分黑色块和蓝色块 
class Solution:
    def trap(self, height: List[int]) -> int:
        #双指针 求每一层两个指针之间的体积（黑色加蓝色）  
        #每一层的体积之和减去所有黑色块就是蓝色块的体积
        #总体积V
        if not height:
            return 0
        V = 0
        n = len(height)
        #左右指针和当前层数
        i,j,f = 0,n-1,1
        while i <= j:
            while (i <= j) and (height[i] < f):
                i += 1
            while (j >= i) and (height[j] < f):
                j -= 1
            f += 1
            V += j - i + 1
        return V-sum(height)