# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

# %%


class Solution(object):
    def containsDuplicate(self, nums) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums or len(nums) == 1:
            return False

        counter = set()

        for n in nums:
            if n not in counter:
                counter.add(n)
            else:
                return True
        return False


# %%

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
nums = []
Solution().containsDuplicate(nums)
