# 88. Merge Sorted Array
# Easy
#
# 1620
#
# 3504
#
# Add to List
#
# Share
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:n] = nums2
            return

        nums1[m:m + n] = nums2

        i = m
        while i < m + n:
            j = i
            while j >= 1:
                if nums1[j - 1] <= nums1[j]:
                    break
                else:
                    nums1[j - 1], nums1[j] = nums1[j], nums1[j - 1]
                    j = j - 1
            i = i + 1


nums1 = [-12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
m = 1
nums2 = [-49, -45, -42, -41, -40, -39, -39, -39, -38, -36, -34, -34, -33, -33, -32, -31, -29, -28, -26, -26, -24, -21, -20, -20, -18, -16, -16, -14, -11, -7, -6, -5, -4, -4, -3, -3, -2, -2, -1,
         0, 0, 0, 2, 2, 6, 7, 7, 8, 10, 10, 13, 13, 15, 15, 16, 17, 17, 19, 19, 20, 20, 20, 21, 21, 22, 22, 24, 24, 25, 26, 27, 29, 30, 30, 30, 35, 36, 36, 36, 37, 39, 40, 41, 42, 45, 46, 46, 46, 47, 48]
n = 90

nums1[m:m + n] = nums2
i = m
while i < m + n:
    j = i
    while j >= 1:
        if nums1[j - 1] <= nums1[j]:
            break
        else:
            nums1[j - 1], nums1[j] = nums1[j], nums1[j - 1]
            j = j - 1
    i = i + 1

nums1

Solution().merge(nums1, m, nums2, n)
len(nums1)

nums2[62]
nums2[62 + 1]
len(nums2)
