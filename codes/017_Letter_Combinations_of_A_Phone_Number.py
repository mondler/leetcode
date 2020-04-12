# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# 17. Letter Combinations of a Phone Number
# Medium
#
# 3369
#
# 379
#
# Add to List
#
# Share
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#
# Accepted
# 552,791
# Submissions
# 1,219,528

# %% DFS ~32ms


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        n = len(digits)
        if n == 0:
            return []

        index = dict()
        index['2'] = {'a', 'b', 'c'}
        index['3'] = {'d', 'e', 'f'}
        index['4'] = {'g', 'h', 'i'}
        index['5'] = {'j', 'k', 'l'}
        index['6'] = {'m', 'n', 'o'}
        index['7'] = {'p', 'q', 'r', 's'}
        index['8'] = {'t', 'u', 'v'}
        index['9'] = {'w', 'x', 'y', 'z'}

        ans = set()
        word = [' ' for _ in range(n)]

        def DFS(word, curr_digit):
            # curr_digit = len(word)
            if curr_digit == n:
                ans.add(''.join(word))
            else:
                for letter in index[digits[curr_digit]]:
                    word[curr_digit] = letter
                    DFS(word, curr_digit + 1)

        DFS(word, 0)

        ans = [a for a in ans]

        return ans


# %% BFS ~44ms


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        n = len(digits)
        if n == 0:
            return []

        index = dict()
        index['2'] = {'a', 'b', 'c'}
        index['3'] = {'d', 'e', 'f'}
        index['4'] = {'g', 'h', 'i'}
        index['5'] = {'j', 'k', 'l'}
        index['6'] = {'m', 'n', 'o'}
        index['7'] = {'p', 'q', 'r', 's'}
        index['8'] = {'t', 'u', 'v'}
        index['9'] = {'w', 'x', 'y', 'z'}

        words = {''}

        for digit in digits:
            tmp = set()
            for word in words:
                for letter in index[digit]:
                    tmp.add(word + letter)
            words = tmp

        return words


# %%
Solution().letterCombinations('23')
Solution().letterCombinations('')
