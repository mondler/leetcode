# https://leetcode.com/problems/surrounded-regions/
# 130. Surrounded Regions
# Medium
#
# 1257
#
# 567
#
# Add to List
#
# Share
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
#
# Accepted
# 193,530
# Submissions
# 751,490


# %% DFS ~132ms # label 'O' connected to boundary; the rest 'O' are surrounded
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        h = len(board)
        if h == 0:
            return
        w = len(board[0])
        if w == 0:
            return

        def DFS(r, c):  # label cells connected to 'O' in boarders
            if r < 0 or r >= h or c < 0 or c >= w or board[r][c] == 'X':
                return
            if board[r][c] == 'O':  # 'O' labels unvisited cell
                board[r][c] = 'D'
                DFS(r - 1, c)
                DFS(r + 1, c)
                DFS(r, c - 1)
                DFS(r, c + 1)

        # horizontal boarder
        for r in range(h):
            DFS(r, 0)
            DFS(r, w - 1)

        # vertical boarder
        for c in range(w):
            DFS(0, c)
            DFS(h - 1, c)

        import itertools

        for r, c in itertools.product(range(h), range(w)):
            if board[r][c] == 'D':
                board[r][c] = 'O'
            else:
                board[r][c] = 'X'


# %%
board = [["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"],
         ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"]]


Solution().solve(board)
board
