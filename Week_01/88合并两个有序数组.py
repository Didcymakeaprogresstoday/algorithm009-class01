# 自己尝试 双指针 时间复杂度O(m+n) 代码不够简洁
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = 0,0,0
        nums1_copy = nums1[0:m]
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                k += 1
                i += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                j += 1
        while i < m or j < n:
            if i<m:
                nums1[k] = nums1_copy[i]
                k += 1
                i += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                j += 1

#改进 将nums清空 直接将每个元素一次添加到清空的数组
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = 0,0,0
        nums1_copy = nums1[0:m]
        nums1[:] = []
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1.append(nums1_copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        nums1 += nums1_copy[i:m] if i<m else nums2[j:n]