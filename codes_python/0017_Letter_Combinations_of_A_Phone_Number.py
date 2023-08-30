#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (54.65%)
# Likes:    12279
# Dislikes: 751
# Total Accepted:    1.3M
# Total Submissions: 2.4M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#

# @lc code=start
class Solution:
    def letterCombinations2(self, digits: str) -> List[str]:
        def DFS(digits, index, l, cur, ans):
            if l == len(digits):
                if l > 0:
                    ans.append("".join(cur))
                return
            # print(digits[l])
            for c in index[digits[l]]:
                cur[l] = c
                DFS(digits, index, l + 1, cur, ans)
            return
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

        cur = [' ' for _ in range(len(digits))]
        ans = []
        DFS(digits, index, 0, cur, ans)
        return ans

    def letterCombinations(self, digits):
        # BFS
        if not digits:
            return []
        d = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for digit in digits:
            tmp = []
            for s in ans:
                for c in d[ord(digit) - ord('0')]:
                    tmp.append(s + c)
            ans = tmp
        return ans

# @lc code=end
