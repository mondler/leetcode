# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 34. Find First and Last Position of Element in Sorted Array
# Medium
#
# 2658
#
# 119
#
# Add to List
#
# Share
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Accepted
# 427,215
# Submissions
# 1,216,635

# %%


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # find first position
        # if not found, return where it should be
        def findFirst(nums, target):
            n = len(nums)
            if target > nums[-1]:  # corner case, return correct insert pos
                return 0, n
            if target < nums[0]:
                return 0, 0
            if n == 1:
                if nums[0] == target:
                    return 1, 0
                else:
                    return 0, nums[0] < target
            left, right = 0, n - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            if nums[left] == target:
                return 1, left
            else:
                return 0, left  # if not found, return where it should be

        if not nums:
            return [-1, -1]
        firstFound, firstPos = findFirst(nums, target)
        if not firstFound:  # if target not found
            return [-1, -1]

        # look for (target + 1)'s first position
        # looking for lastPos from firstPos to end
        lastPos = findFirst(nums[firstPos:], target + 1)[1] - 1 + firstPos

        return [firstPos, lastPos]


# %%
nums = [5, 7, 7, 8, 8, 10]
target = 8
Solution().searchRange(nums, target)


arr = [4, 3, 2, 1]
i = 0
min(arr[i - 1:i] + arr[i + 1:i + 2])
min(arr[i - 1], arr[i + 1])
