# https://leetcode.com/problems/word-search/description/
# 79. Word Search
# Medium
#
# 3032
#
# 155
#
# Add to List
#
# Share
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
# Constraints:
#
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# Accepted
# 415,679
# Submissions
# 1,222,434


# %% DFS + backtracking ~364ms
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        h = len(board)
        w = len(board[0])

        n = len(word)

        cells_used = set()

        def DFS(r, c, i_word):
            if i_word == n:
                return True
            if r < 0 or r >= h or c < 0 or c >= w or board[r][c] != word[i_word] or (r, c) in cells_used:
                return False

            cells_used.add((r, c))

            ans = DFS(r - 1, c, i_word + 1) or \
                DFS(r + 1, c, i_word + 1) or \
                DFS(r, c - 1, i_word + 1) or \
                DFS(r, c + 1, i_word + 1)

            if ans:  # if whole word found in certain direction
                return True

            # backtracking
            cells_used.discard((r, c))
            return False

        # found word starting from every cell using DFS
        from itertools import product
        for r, c in product(range(h), range(w)):
            if DFS(r, c, 0):
                return True

        return False


# %%


board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCB"
Solution().exist(board, word)
