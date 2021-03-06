# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0


class Solution:
    def searchInsert(self, nums, target):
        N = len(nums)
        if N == 0:
            return 0
        left = 0
        right = N - 1
        while right - left > 0:
            mid = (right - left + 1) // 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[right] < target:
            return (right + 1)
        else:
            return right


nums = [1, 3, 5, 7, 7, 9]
target = 7
Solution().searchInsert(nums, target)


len(nums)
nums[5229]
nums[3919]
