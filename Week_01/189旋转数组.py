#第一尝试  复杂度为O(k%n*n)  超时
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = [0] 
        n = len(nums)
        for i in range(k%n):
            d = nums[n-1]
            for j in range(n-1,0,-1):
                nums[j] = nums[j-1]
            nums[0] = d

# 第二次尝试  三次反转法  时间复杂度O(n) 空间复杂度O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        def swap(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        swap(0,n-k-1)
        swap(n-k,n-1)
        swap(0,n-1)            
