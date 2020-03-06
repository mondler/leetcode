# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# 153. Find Minimum in Rotated Sorted Array
# Medium
#
# 1624
#
# 210
#
# Add to List
#
# Share
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
# Accepted
# 380,157
# Submissions
# 859,967

# %%


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


# %%
Solution().findMin([3, 4, 5, 1, 2])
Solution().findMin([4, 5, 6, 7, 0, 1, 2])
