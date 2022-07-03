#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (38.09%)
# Likes:    15389
# Dislikes: 958
# Total Accepted:    1.6M
# Total Submissions: 4.1M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
#
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
#
#
#

# %%
# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            # if left half intact; eg: [4, 5, 6, 7, 0, 1, 2]
            if nums[mid] >= nums[low]:
                if (nums[mid] > target) and (nums[low] <= target):
                    high = mid - 1
                else:
                    low = mid + 1
            # else, right half intact; eg: [4, 5, 0, 1, 2]
            else:
                if (nums[mid] < target) and (nums[high] >= target):
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    def search_bf(self, nums: list[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
        return -1


# @lc code=end


# %%
nums = [4, 5, 6, 7, 0, 1, 2]
target = 2

print(target)

# %%
Solution().search(nums, target)

# %%
print(
    f"The index of target in nums is {Solution().search(nums, target)} by solution and {Solution().search_bf(nums, target)} by brute force"
)
