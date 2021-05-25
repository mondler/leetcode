# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
#
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

# %%


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > max:
                    max = count
                count = 0

        if count > max:
            max = count

        return max


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.append(0)

        maxOne = 0
        lastZero = -1

        for i, num in enumerate(nums):
            if num == 1:
                continue
            currentOne = i - lastZero - 1
            if currentOne > maxOne:
                maxOne = currentOne
            lastZero = i

        return maxOne


# %%
nums = [1, 1, 0, 1, 1, 1]

Solution().findMaxConsecutiveOnes(nums)
