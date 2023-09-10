# https://leetcode.com/problems/sort-colors/description/
#
# Medium
#
# 2492
#
# 192
#
# Add to List
#
# Share
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:
#
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?


# %% dutch colors
class Solution1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i_zero = 0
        i_curr = 0
        i_two = len(nums) - 1

        while i_curr <= i_two:
            if nums[i_curr] == 0:
                nums[i_zero], nums[i_curr] = nums[i_curr], nums[i_zero]
                i_zero += 1
                i_curr += 1
            elif nums[i_curr] == 2:
                nums[i_two], nums[i_curr] = nums[i_curr], nums[i_two]
                i_two -= 1
            else:
                i_curr += 1
                # %% quicksort; 1 as pivot


# %% quicksort; random pivot
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def quicksort(nums, left, right):
            if left < right:
                j = self.partition(nums, left, right)
                quicksort(nums, left, j - 1)
                quicksort(nums, j + 1, right)

        quicksort(nums, 0, len(nums) - 1)

    def partition(self, nums, left, right):
        import random

        pivot = random.randint(left, right)
        nums[right], nums[pivot] = nums[pivot], nums[right]
        j = left  # place to put next low element
        for i in range(left, right):
            if nums[i] < nums[right]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        if j < right:
            nums[j], nums[right] = nums[right], nums[j]
        return j


# %%
nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)
