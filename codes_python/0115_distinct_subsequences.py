#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (45.24%)
# Likes:    6382
# Dislikes: 280
# Total Accepted:    360.9K
# Total Submissions: 783.9K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given two strings s and t, return the number of distinct subsequences of s
# which equals t.
# 
# The test cases are generated so that the answer fits on a 32-bit signed
# integer.
# 
# 
# Example 1:
# 
# 
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# 
# 
# Example 2:
# 
# 
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.
# 
# 
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # s longer string
        # t: to be matched
        # dynamic programming
        # dp[i][j]: number of subseq in s using first i characters equal to first j characters of t
        ls = len(s)
        lt = len(t)
        dp = [[0] * (lt + 1) for _ in range(ls + 1)]

        for i in range(ls+1):
            dp[i][0] = 1

        for j in range(1, lt+1):
            for i in range(1, ls+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[ls][lt]

# s = 'bagg'
# t = 'bag'

# print(Solution().numDistinct(s, t))
# @lc code=end

