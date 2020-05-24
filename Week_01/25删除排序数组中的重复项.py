#个人第一次尝试
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        time,n = 0,len(nums)
        i,j = 0,0
        d = {}
        while j < len(nums):
            if nums[j] in d:
                j += 1
                continue
            else:
                d.setdefault(nums[j],1)
                nums[i] = nums[j]
                i += 1
                time += 1
                j += 1
        return time

#参考后改进  没必要写得很复杂 判断两个指针指向的元素是不是相等就可以
#不用创建hash表
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        for j in range(1,n):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1