#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (34.88%)
# Likes:    17198
# Dislikes: 526
# Total Accepted:    1.1M
# Total Submissions: 3.1M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a subarray that has the largest product,
# and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
#
#
# Example 1:
#
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#


# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """Save current max pos and current max neg; update with new num in nums

        Args:
            nums (list[int]): _description_

        Returns:
            int: _description_
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        curPos = max(0, nums[0])
        curNeg = min(0, nums[0])
        maxPos = curPos
        maxNeg = curNeg
        for n in nums[1:]:
            if n == 0:
                curPos = 0
                curNeg = 0
            elif n > 0:
                curPos = n * max(curPos, 1)
                curNeg = n * curNeg
            else:
                curPos, curNeg = n * curNeg, n * max(curPos, 1)
            # print(n, curPos, curNeg)
            maxPos = max(curPos, maxPos)
            maxNeg = min(curNeg, maxNeg)
        return maxPos


# solution = Solution()
# # nums = [2, 3, -2, 4]
# nums = [-2, 0, -1]
# print(solution.maxProduct(nums))

# @lc code=end
