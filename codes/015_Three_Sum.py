# https://leetcode.com/problems/3sum/
# 15. 3Sum
# Medium
#
# 10434
#
# 1068
#
# Add to List
#
# Share
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []
#
#
#
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []

        nums.sort()

        l = len(nums)

        for i in range(l):
            n1 = nums[i]
            if n1 > 0:
                break

            if ((i > 0) and (n1 == nums[i - 1])):
                continue

            j = i + 1
            k = l - 1

            while (j < k):
                n2 = nums[j]
                n3 = nums[k]
                s = n1 + n2 + n3

                if s == 0:
                    res.append([n1, n2, n3])
                    while ((j < l) and (nums[j] == n2)):
                        j += 1
                    while ((k > j) and (nums[k] == n3)):
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return res


# %%
nums = [-1, 0, 1, 2, -1, -4]

Solution().threeSum(nums)
