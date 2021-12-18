# 633. Sum of Square Numbers
# Easy
#
# 418
#
# 279
#
# Add to List
#
# Share
# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
#
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
#
#
# Example 2:
#
# Input: 3
# Output: False

# %%


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        a, b = 0, int(c**0.5)

        while a <= b:
            d = a * a + b * b
            if d == c:
                return True

            elif d > c:
                b -= 1
            else:
                a += 1

        return False


# %%

c = 5
Solution().judgeSquareSum(c)
