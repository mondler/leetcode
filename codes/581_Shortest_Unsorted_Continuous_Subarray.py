# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
#
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
#
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

# %%


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        nums2 = sorted(nums)
        i, j = 0, n - 1
        while i < n and nums[i] == nums2[i]:
            i += 1
        while j >= i and nums[j] == nums2[j]:
            j -= 1
        return j - i + 1


# %%


nums = [2, 6, 4, 8, 10, 9, 15]
nums[-1]

nums = [1, 2, 3, 4]

Solution().findUnsortedSubarray(nums)


nums
nums[:-1]
nums[1:]

sum(nums)
