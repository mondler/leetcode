# https://leetcode.com/problems/max-area-of-island/description/
# 695. Max Area of Island
# Medium
#
# 1587
#
# 72
#
# Add to List
#
# Share
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.
#
# Accepted
# 131,335
# Submissions
# 215,582


# %% DFS ~136ms
# similar to 200: Number of Islands


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])

        self.grid = grid

        ans = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 0:
                    continue
                ans = max(ans, self.__area(r, c, h, w))

        return ans

    def __area(self, r, c, h, w):
        if r < 0 or r >= h or c < 0 or c >= w or self.grid[r][c] == 0:
            return 0

        # if this cell is 1, add 1 to count, reset to zero, and search for all other neighbours
        self.grid[r][c] = 0

        return 1 + self.__area(r - 1, c, h, w) + self.__area(r + 1, c, h, w) + self.__area(r, c - 1, h, w) + self.__area(r, c + 1, h, w)


# %% DFS
# similar to 200: Number of Islands


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])

        def area(r, c):
            if r < 0 or r >= h or c < 0 or c >= w or grid[r][c] == 0:
                return 0

            # if this cell is 1, add 1 to count, reset to zero, and search for all other neighbours
            grid[r][c] = 0

            return 1 + area(r - 1, c) + area(r + 1, c) + area(r, c - 1) + area(r, c + 1)

        ans = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 0:
                    continue
                ans = max(ans, area(r, c))

        return ans



# %%
grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
Solution().maxAreaOfIsland(grid)

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
Solution().maxAreaOfIsland(grid)
