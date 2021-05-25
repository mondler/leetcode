# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# 1091. Shortest Path in Binary Matrix
# Medium
#
# 272
#
# 32
#
# Add to List
#
# Share
# In an N by N square grid, each cell is either empty (0) or blocked (1).
#
# A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:
#
# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
# Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
#
#
#
# Example 1:
#
# Input: [[0,1],[1,0]]
#
#
# Output: 2
#
# Example 2:
#
# Input: [[0,0,0],[1,1,0],[1,1,0]]
#
#
# Output: 4
#
#
#
# Note:
#
# 1 <= grid.length == grid[0].length <= 100
# grid[r][c] is 0 or 1
# Accepted
# 21,395
# Submissions
# 57,288

# %% Regular BFS


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1  # path not exist

        if n == 1:
            return 1

        # cell locations that need to be explored (open, 0 as value)
        new_cells = {(i, j) for i in range(n)
                     for j in range(n) if grid[i][j] == 0}
        s = {(0, 0)}  # currently at these locs
        target = {(n - 1, n - 1)}
        new_cells = new_cells.difference(s.union(target))
        target = target.pop()
        step = 0
        while len(s) > 0:
            step += 1
            s1 = set()
            for (r, c) in s:
                # explore cells sharing same edge or corner with 0 as value
                new_locs = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                            (r, c - 1), (r, c + 1),
                            (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
                for new_loc in new_locs:
                    if new_loc == target:
                        return step + 1
                    if new_loc not in new_cells:
                        continue
                    new_cells.remove(new_loc)
                    s1.add(new_loc)
            s = s1
        return -1


# %% Bidirectional BFS


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # grid = [[0, 1], [1, 0]]
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1  # path not exist

        if n == 1:
            return 1

        # cell locations that need to be explored (open, 0 as value)
        new_cells = {(i, j) for i in range(n)
                     for j in range(n) if grid[i][j] == 0}

        s1 = {(0, 0)}  # currently at these locs
        s2 = {(n - 1, n - 1)}

        # new_cells = new_cells.difference(s1.union(s2))

        step = 0
        while len(s1) > 0 and len(s2) > 0:
            step += 1

            # s1 always the smaller one
            if len(s1) > len(s2):
                s1, s2 = s2, s1

            s = set()
            for (r, c) in s1:
                # explore cells sharing same edge or corner with 0 as value
                new_locs = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                            (r, c - 1), (r, c + 1),
                            (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
                for new_loc in new_locs:
                    if new_loc in s2:
                        return step + 1
                    if new_loc not in new_cells:
                        continue
                    new_cells.remove(new_loc)
                    s.add(new_loc)
            s1 = s
        return -1


# %%
grid = [[0, 1], [1, 0]]
grid = [[0, 0, 0, 0, 1], [1, 0, 0, 0, 0], [
    0, 1, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0]]
Solution().shortestPathBinaryMatrix(grid)
