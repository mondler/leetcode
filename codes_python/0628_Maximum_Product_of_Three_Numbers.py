# Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
# Example 1:
#
# Input: [1,2,3]
# Output: 6
#
#
# Example 2:
#
# Input: [1,2,3,4]
# Output: 24
#
#
# Note:
#
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

# %% Using sort function


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if (nums[0] > 0) or (nums[-1] < 0):
            return nums[-1] * nums[-2] * nums[-3]
        max2_test1 = nums[0] * nums[1]
        max2_test2 = nums[-2] * nums[-3]
        max2 = max(max2_test1, max2_test2)
        return max2 * nums[-1]


# %% Using Heap to find maximum k numbers (O(n*log(3)))

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import heapq
        a = heapq.nlargest(3, nums)  # from largest to smaller
        b = heapq.nsmallest(2, nums)  # from smallest to larger
        return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])


# %%
nums = [-8, -6, -5, 4, 7, 9]
Solution().maximumProduct(nums)
