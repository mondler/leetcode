# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


# %%


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return int(n * (n + 1) / 2 - sum(nums))

# %%


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mySet = set(nums)
        n = len(nums)
        for i in range(n):
            if i not in mySet:
                return i
        return n


# %%


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        result = set(range(len(nums) + 1))

        for n in nums:
            result.remove(n)

        return result.pop()


# %%
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Solution().missingNumber(nums)
