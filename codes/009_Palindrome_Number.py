# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads - 121. From right to left, it becomes 121 - . Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Could you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        return self.reverse(x) == x

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

        return rev
        # if -(2 ** 31) <= rev < 2 ** 31 else 0


x = 12321
Solution().isPalindrome(x)
