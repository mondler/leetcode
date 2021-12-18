# 345. Reverse Vowels of a String
# Easy
#
# 531
#
# 946
#
# Add to List
#
# Share
# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".

# %%


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] in vowels:
                if s[j] in vowels:
                    s[i], s[j] = s[j], s[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1

        return "".join(s)


# %%
s = 'leetcode'
Solution().reverseVowels(s)
