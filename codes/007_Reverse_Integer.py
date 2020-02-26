# Given a 32 - bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32 - bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# Solution: divide by 10, multiply previous res by 10, plus module

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        sign = 1 if x > 0 else -1
        x = x * sign

        rev = 0
        while x != 0:
            x, rev = x // 10, rev * 10 + x % 10

        rev = rev * sign

        return rev if -(2 ** 31) <= rev < 2 ** 31 else 0


x = -3210

rev = Solution().reverse(x)
