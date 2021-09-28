# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# 451. Sort Characters By Frequency
# Medium
#
# 1032
#
# 90
#
# Add to List
#
# Share
# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
# Accepted
# 127,693
# Submissions
# 217,210

# %%


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        frq = Counter(s).most_common()
        output = ''.join([item[0] * item[1] for item in frq])
        return output


# %%
s = "bbAa"
Solution().frequencySort(s)
