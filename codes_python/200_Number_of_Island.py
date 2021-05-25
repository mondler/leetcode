# https://leetcode.com/problems/number-of-islands/
# 200. Number of Islands
# Medium
#
# 4487
#
# 163
#
# Add to List
#
# Share
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
# Accepted
# 590,592
# Submissions
# 1,306,210

# %% DFS, similar to 695, ~144ms


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        h = len(grid)
        if h == 0:
            return 0
        w = len(grid[0])
        if w == 0:
            return 0

        def modify_island(r, c):
            if r < 0 or r >= h or c < 0 or c >= w or grid[r][c] == "0":
                return 0

            # if this cell is 1, reset to zero, and reset all other neighbours
            grid[r][c] = "0"
            modify_island(r - 1, c)
            modify_island(r + 1, c)
            modify_island(r, c - 1)
            modify_island(r, c + 1)
            return 1

        ans = 0
        for r in range(h):
            for c in range(w):
                ans += modify_island(r, c)

        return ans


# %%
grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]

Solution().numIslands(grid)
