#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (54.56%)
# Likes:    16690
# Dislikes: 386
# Total Accepted:    1.8M
# Total Submissions: 3.3M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(grid, x, y, r, c):
            if (x < 0) or (x >= r) or (y < 0) or (y >= c) or (grid[x][y] == '0'):
                return
            grid[x][y] = '0'
            DFS(grid, x+1, y, r, c)
            DFS(grid, x - 1, y, r, c)
            DFS(grid, x, y + 1, r, c)
            DFS(grid, x, y - 1, r, c)

        if len(grid) == 0:
            return 0
        r, c = len(grid), len(grid[0])
        ans = 0
        for x in range(r):
            for y in range(c):
                if grid[x][y] == '1':
                    ans += 1
                    DFS(grid, x, y, r, c)
        return ans


# @lc code=end
