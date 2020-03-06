# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
# 744. Find Smallest Letter Greater Than Target
# Easy
#
# 316
#
# 443
#
# Add to List
#
# Share
# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
#
# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
#
# Examples:
#
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"
#
# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:
#
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique letters.
# target is a lowercase letter.
# Accepted
# 60,358
# Submissions
# 134,518


# %% binary search


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1]:
            return letters[0]
        left = 0
        right = len(letters) - 1
        while left < right:
            mid = right + (left - right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        return letters[right]


# %%
letters = ["c", "f", "j"]
target = "j"
Solution().nextGreatestLetter(letters, target)
