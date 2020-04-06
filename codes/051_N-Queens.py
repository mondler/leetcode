# https://leetcode.com/problems/n-queens/
# 51. N-Queens
# Hard
#
# 1544
#
# 65
#
# Add to List
#
# Share
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
# Accepted
# 185,121
# Submissions
# 417,415


# %% DFS + Backtracking ~156ms
# https://zxi.mytechroad.com/blog/searching/leetcode-51-n-queens/
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # record col, diag1, diag2 with queen already
        self.col_fill = set()
        self.diag1_fill = set()  # northeast diagnol
        self.diag2_fill = set()  # southeast diagonal

        self.solutions = []
        self.board = [['.' for i in range(n)] for j in range(n)]

        self.start_fill(n, 0)

        return self.solutions

    def not_fillable(self, r, c):
        return (
            (c in self.col_fill)
            or
            ((r + c) in self.diag1_fill)
            or
            ((r - c) in self.diag2_fill)
        )

    def update_board(self, n, r, c, is_fill):
        if is_fill:
            self.board[r][c] = 'Q'
            self.col_fill.add(c)
            self.diag1_fill.add(r + c)
            self.diag2_fill.add(r - c)
        else:
            self.board[r][c] = '.'
            self.col_fill.discard(c)
            self.diag1_fill.discard(r + c)
            self.diag2_fill.discard(r - c)

    def start_fill(self, n, r):
        # fill the board row by row
        if r == n:  # if all filled
            self.solutions.append([''.join(s) for s in self.board])
            return

        for c in range(n):  # try each col to fill queen
            if self.not_fillable(r, c):
                # pass to next col if pos not available
                continue

            # try filling queen into r, c
            self.update_board(n, r, c, is_fill=True)

            # DFS
            self.start_fill(n, r + 1)

            # Backtracking
            self.update_board(n, r, c, is_fill=False)


# %% Concise version: DFS + Record cols to put queens ~80ms

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []

        def DFS(cols, diag1, diag2):
            r = len(cols)  # current row to deal with
            if r == n:
                result.append(["." * c + "Q" + "." * (n - c - 1)
                               for c in cols])

            for c in range(n):
                if ((c not in cols) and ((r + c) not in diag1) and ((r - c) not in diag2)):
                    # filling queen in col c without changing current cols
                    DFS(cols + [c], diag1 + [r + c], diag2 + [r - c])

        DFS([], [], [])

        return result


# %%
Solution().solveNQueens(4)
