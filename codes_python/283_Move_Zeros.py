# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        flag_found_zero = False  # loc of first zero

        for i, n in enumerate(nums):
            if (not flag_found_zero):
                if n == 0:
                    j = i  # index of first zero
                    flag_found_zero = True
            elif (n != 0):
                nums[j], nums[i] = n, 0
                j += 1   # update index of first zero


# %%

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        loc = 0  # next place to put non-zero
        for i, n in enumerate(nums):
            if n:
                nums[loc] = n
                loc += 1

        for i in range(loc, len(nums)):
            nums[i] = 0

# %%


nums = [2, 1]
Solution().moveZeroes(nums)
nums
