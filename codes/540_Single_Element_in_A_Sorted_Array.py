# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# 40. Single Element in a Sorted Array
# Medium
#
# 1049
#
# 72
#
# Add to List
#
# Share
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
#
#
#
# Example 1:
#
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
#
# Input: [3,3,7,7,10,11,11]
# Output: 10
#
#
# Note: Your solution should run in O(log n) time and O(1) space.
#
# Accepted
# 77,447
# Submissions
# 134,396

# %%


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 1:
                mid = mid - 1
            if nums[mid] == nums[mid + 1]:  # left of target would pair up
                left = mid + 2
            else:
                right = mid
        return nums[left]


# %%
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
Solution().singleNonDuplicate(nums)
