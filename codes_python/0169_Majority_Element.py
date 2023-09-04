# @lc app=leetcode id=169 lang=python3

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2


# %%
# @lc code=start
# class Solution:
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         ct = {}
#         for num in nums:
#             if num in ct:
#                 ct[num] += 1
#             else:
#                 ct[num] = 1
#         majority = max(ct, key=ct.get)
#         return majority


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        occ_major = l / 2
        ct = {}
        for num in nums:
            if num in ct:
                ct[num] += 1
            else:
                ct[num] = 1

            if ct[num] > occ_major:
                return num

        return -1


# @lc code=end


nums = [3, 2, 3, 2, 2]
print(Solution().majorityElement(nums))

# $300
# 6002 0000 0204 9562
# 0097

# $50
# 6019 0002 8419 3295
# 2560
