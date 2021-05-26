# 70. Climbing Stairs
# Easy
#
# 6665
#
# 212
#
# Add to List
#
# Share
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
# Constraints:
#
# 1 <= n <= 45
# Accepted
# 972,056
# Submissions
# 1,987,673

class Solution:
    def __init__(self):
        self.results = {
            1: 1,
            2: 2
        }

    # recursion
    def climbStairs(self, n: int) -> int:
        if n not in self.results:
            self.results[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.results[n]

    # no recursion
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        a = b = 1
        for _ in range(n - 1):
            a, b = a + b, a
        return a

    # no recursion
    def climbStairs3(self, n: int) -> int:
        if n <= 2:
            return n
        results = [0] * n
        results[0] = 1
        results[1] = 2
        for i in range(2, n):
            results[i] = results[i - 2] + results[i - 1]
        return results[-1]

        # %%
Solution().climbStairs(8)
Solution().climbStairs2(8)
Solution().climbStairs3(8)

a = [0] * 8
len(a)
