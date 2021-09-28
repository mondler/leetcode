# https://leetcode.com/problems/non-decreasing-array/description/
# 665. Non-decreasing Array
# Easy
#
# 1524
#
# 360
#
# Add to List
#
# Share
# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
# Example 1:
#
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
#
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].
#
# Accepted
# 78,869
# Submissions
# 405,763

# %%


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 2:
            return True
        cnt = 0
        if nums[1] < nums[0]:
            nums[0] = nums[1]
            cnt += 1
        for i in range(2, n):
            if nums[i] < nums[i - 1]:
                cnt += 1
                if cnt == 2:
                    return False
                if nums[i] < nums[i - 2]:
                    # less desirable case: make smaller number big
                    nums[i] = nums[i - 1]
                else:
                    # prefer to make large number smaller
                    nums[i - 1] = nums[i]
        return True


# %%
nums = [2, 3, 3, 2, 4]
Solution().checkPossibility(nums)
nums = [4, 2, 3]
Solution().checkPossibility(nums)
nums = [4]
Solution().checkPossibility(nums)
