# https://leetcode.com/problems/pacific-atlantic-water-flow/
# 417. Pacific Atlantic Water Flow
# Medium
#
# 1039
#
# 203
#
# Add to List
#
# Share
# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
#
# Note:
#
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
#
#
# Example:
#
# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
#
#
# Accepted
# 65,861
# Submissions
# 165,222


# %% DFS ~288ms
# start from edge, get nodes reachable from Pacafic/Atlantic
# use set to save result


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        h = len(matrix)
        if h == 0:
            return []
        w = len(matrix[0])
        if w == 0:
            return []

        def DFS(r, c, height, nodes):
            if r < 0 or r == h or c < 0 or c == w or (r, c) in nodes:
                return

            curr_height = matrix[r][c]
            if curr_height >= height:
                nodes.add((r, c))
                DFS(r + 1, c, curr_height, nodes)
                DFS(r - 1, c, curr_height, nodes)
                DFS(r, c + 1, curr_height, nodes)
                DFS(r, c - 1, curr_height, nodes)

        p_nodes = set()
        for c in range(w):
            DFS(0, c, 0, p_nodes)
        for r in range(h):
            DFS(r, 0, 0, p_nodes)

        a_nodes = set()
        for c in range(w):
            DFS(h - 1, c, 0, a_nodes)
        for r in range(h):
            DFS(r, w - 1, 0, a_nodes)

        # ans = []
        # for p in p_nodes:
        #     if p in a_nodes:
        #         ans.append(p)

        ans = p_nodes.intersection(a_nodes)
        ans = [[t[0], t[1]] for t in ans]
        return ans


# %%
matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]

Solution().pacificAtlantic(matrix)
