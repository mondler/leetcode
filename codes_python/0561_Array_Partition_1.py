# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Example 1:
#
# Input: [1,4,3,2]
#
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# Note:
#
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].


# %%
class Solution():
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)

        return sum(nums[::2])


# %% use 20001 array index to label number, array value to save # occurence

class Solution2():
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occ = [0] * 20001

        for n in nums:
            occ[n + 10000] += 1

        # for n in nums:
        #     print(f'{n}: {occ[n + 10000]}')

        l = len(nums) // 2
        count = 0
        nextIsFirst = True
        res = 0

        for i, o in enumerate(occ):  # i is a n in nums, o is its occurence
            if count == l:
                break
            if o > 0:
                for j in range(o):

                    if nextIsFirst:
                        res += i - 10000
                        count += 1
                        nextIsFirst = False
                        # print(f'{i-10000} is added')
                    else:
                        nextIsFirst = True

        return res

# %%


nums = [6, 2, 6, 5, 1, 2]  # 1, 2, 2, 5, 6, 6 --> 1 + 2 + 6 = 9

# print(Solution().arrayPairSum(nums))
print(Solution2().arrayPairSum(nums))
