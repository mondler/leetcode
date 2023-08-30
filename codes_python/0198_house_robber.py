#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (47.71%)
# Likes:    18577
# Dislikes: 345
# Total Accepted:    1.7M
# Total Submissions: 3.4M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        hightest_w_cur = []  # highest with the current index robbed
        l = len(nums)
        if l <= 2:
            return max(nums)

        if l == 3:
            return max(nums[1], nums[0] + nums[2])

        hightest_w_cur.append(nums[0])
        hightest_w_cur.append(nums[1])
        hightest_w_cur.append(nums[0] + nums[2])

        for i in range(3, l):
            # highest with the current index robbed is i-2 + nums[i] or i-3 + nums[i]
            hightest_w_cur.append(max(hightest_w_cur[-2], hightest_w_cur[-3]) + nums[i])

        return max(hightest_w_cur[-2], hightest_w_cur[-1])

# @lc code=end


solution = Solution()

print(solution.rob(nums=[2, 1, 1, 2]))
