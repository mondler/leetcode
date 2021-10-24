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

# Solution().findDisappearedNumbers(nums)


# %% 20211013

class Solution2:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # if n appears n nums, modify the sign of nums[n-1] to record it
        for n in nums:
            idx = abs(n) - 1
            nums[idx] = -1 * abs(nums[idx])
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res


# %%
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution2().findDisappearedNumbers(nums))

nums = [2, 2]
print(Solution2().findDisappearedNumbers(nums))


# %%

# a = [2, 1, 2]
# b = set(a)
# b
# c = {1}
# c
# b - c
#
# for n in b:
#     print(n)
