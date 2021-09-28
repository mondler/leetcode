# Given an array of integers where 1 ≤ a[i] ≤ n(n=size of array), some elements appear twice and others appear once.
#
# Find all the elements of[1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4, 3, 2, 7, 8, 2, 3, 1]
#
# Output:
# [5, 6]

# %%


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for num in nums:
            index = abs(num) - 1  # if a num exist
            nums[index] = -abs(nums[index])  # make one element negative

        a = [i + 1 for i, num in enumerate(nums) if num > 0]

        return a

# %%


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return list(set(range(1, len(nums) + 1)) - set(nums))


# %%

nums = [4, 3, 2, 7, 8, 2, 3, 1]

Solution().findDisappearedNumbers(nums)
