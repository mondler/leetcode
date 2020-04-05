# https://leetcode.com/problems/sudoku-solver/
# 37. Sudoku Solver
# Hard
#
# 1461
#
# 83
#
# Add to List
#
# Share
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique solution.
# The given board size is always 9x9.
# Accepted
# 169,581
# Submissions
# 409,666


# %% DFS + backtracking + dict of set   ~92ms
# https://zxi.mytechroad.com/blog/searching/leetcode-37-sudoku-solver/


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        import collections
        # record numbers appearing in each row, col, box
        row_fill = collections.defaultdict(set)
        col_fill = collections.defaultdict(set)
        box_fill = collections.defaultdict(set)

        for r, row in enumerate(board):
            for c, v in enumerate(row):
                if v != '.':
                    row_fill[r].add(v)
                    col_fill[c].add(v)
                    box_id = 3 * (r // 3) + c // 3
                    box_fill[box_id].add(v)

        self.board = board
        self.row_fill = row_fill
        self.col_fill = col_fill
        self.box_fill = box_fill
        self.start_fill(0, 0)

    def start_fill(self, r, c):
        if r == 9:  # if all filled
            return True

        next_c = (c + 1) % 9
        if next_c == 0:
            next_r = r + 1
        else:
            next_r = r

        if self.board[r][c] != '.':
            return self.start_fill(next_r, next_c)

        box_id = 3 * (r // 3) + c // 3
        for num in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            if (num in self.row_fill[r] or num in self.col_fill[c] or num in self.box_fill[box_id]):
                # pass to next num if already existed in same row, col, box
                continue

            # try filling num into r, c
            self.row_fill[r].add(num)
            self.col_fill[c].add(num)
            self.box_fill[box_id].add(num)
            self.board[r][c] = num

            if (self.start_fill(next_r, next_c)):
                # continue and return True if all filled out successfully
                return True
            else:  # backtracking
                self.board[r][c] = '.'
                self.row_fill[r].discard(num)
                self.col_fill[c].discard(num)
                self.box_fill[box_id].discard(num)
        return False


# %% DFS + backtracking ~200ms
# https://zxi.mytechroad.com/blog/searching/leetcode-37-sudoku-solver/


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # row_fill[i][n] == 1 if n is used in ith row
        row_fill = [[0 for i in range(10)] for j in range(9)]
        # col_fill[i][n] == 1 if n is used in ith col
        col_fill = [[0 for i in range(10)] for j in range(9)]
        # box_fill[i][n] == 1 if n is used in ith box
        box_fill = [[0 for i in range(10)] for j in range(9)]

        for r, row in enumerate(board):
            for c, v in enumerate(row):
                if v != '.':
                    v = int(v)
                    row_fill[r][v] = 1
                    col_fill[c][v] = 1
                    box_id = 3 * (r // 3) + c // 3
                    box_fill[box_id][v] = 1

        self.board = board
        self.row_fill = row_fill
        self.col_fill = col_fill
        self.box_fill = box_fill
        self.start_fill(0, 0)

    def start_fill(self, r, c):
        if r == 9:  # if all filled
            return True

        next_c = (c + 1) % 9
        if next_c == 0:
            next_r = r + 1
        else:
            next_r = r
        # print('start_fill', (r, c))

        if self.board[r][c] != '.':
            return self.start_fill(next_r, next_c)

        for i in range(1, 10):
            box_id = 3 * (r // 3) + c // 3
            if (self.row_fill[r][i] or self.col_fill[c][i] or self.box_fill[box_id][i]):
                continue  # pass to next number if already filled somewhere
            self.row_fill[r][i] = 1
            self.col_fill[c][i] = 1
            self.box_fill[box_id][i] = 1
            self.board[r][c] = str(i)
            if (self.start_fill(next_r, next_c)):
                return True
            self.board[r][c] = '.'
            self.row_fill[r][i] = 0
            self.col_fill[c][i] = 0
            self.box_fill[box_id][i] = 0
        return False



# %%
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board[2][2]
board[-1][-1]

Solution().solveSudoku(board)

board


# %%
import collections

q = collections.deque([])
for i in range(5):
    q.append(i)

q[0]

while q:
    print(q.popleft())
