# 5. Longest Palindromic Substring
# Medium
#
# 13511
#
# 801
#
# Add to List
#
# Share
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
#
# Input: s = "a"
# Output: "a"
# Example 4:
#
# Input: s = "ac"
# Output: "a"
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# Accepted
# 1,481,875
# Submissions
# 4,742,724

# %%

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def getLen(l, r):
            # return length of longest palindromic expanding from l to r
            while ((l >= 0) and (r < n) and (s[l] == s[r])):
                l -= 1
                r += 1
            # while loops ends with [l+1, r-1] as a valid palindrome
            return r - l - 1

        start = 0
        currMaxLen = 1

        for i in range(n):
            oddLen = getLen(i, i)
            evenLen = getLen(i, i + 1)
            newMaxLen = max(oddLen, evenLen)
            # continue to next run if not exceeding current max len
            if newMaxLen <= currMaxLen:
                continue
            # if exceeding current max len
            currMaxLen = newMaxLen
            start = i - (newMaxLen - 1) // 2

        return s[start:start + currMaxLen]


# %%

s = "bdbbd"

print(Solution().longestPalindrome(s))
