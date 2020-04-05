# https://leetcode.com/problems/perfect-squares/description/
# 279. Perfect Squares
# Medium
#
# 2263
#
# 172
#
# Add to List
#
# Share
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
# Accepted
# 254,286
# Submissions
# 566,183

# %% Dynamic Programming; Add static variable to save results for different runs


class Solution:
    _dp = [0]  # static variable in class to save results

    def numSquares(self, n: int) -> int:
        dp = self._dp
        while len(dp) <= n:
            dp.append(1 + min(dp[- j * j]
                              for j in range(1, int(len(dp)**0.5 + 1))))
        return dp[n]


# %%
ss = Solution()
ss.numSquares(13)
ss._dp

ss.numSquares(28)
ss._dp


# %% BFS

class Solution:
    def numSquares(self, n: int) -> int:
        dp = self._dp
        s = {n}
        step = 0
        while len(s) >= 0:
            step += 1
            s = {i - j * j for i in s for j in range(1, int(n**0.5 + 1))}
            if 0 in s:
                return step


Solution().numSquares(13)
