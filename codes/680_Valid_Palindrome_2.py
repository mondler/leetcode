# 680. Valid Palindrome II
# Easy
#
# 1126
#
# 82
#
# Add to List
#
# Share
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
#
# Input: "aba"
# Output: True
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
#
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

# %%


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        if self.is_palindrome2(s, i, j):
            return True
        while i < j:
            if s[i] != s[j]:
                return self.is_palindrome2(s, i + 1, j) or self.is_palindrome2(s, i, j - 1)
            i += 1
            j -= 1
        return True

    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def is_palindrome2(self, s, i, j):
        a = s[i:j + 1]
        return a == a[::-1]


# %%
s = 'abc'
s[0:3][::-1]
s[3:-1:-1]
print(Solution().is_palindrome(s, 0, len(s) - 1))
print(Solution().validPalindrome(s))
