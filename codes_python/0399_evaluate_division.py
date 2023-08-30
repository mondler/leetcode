#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (58.92%)
# Likes:    6380
# Dislikes: 544
# Total Accepted:    303.5K
# Total Submissions: 512.2K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
'[2.0,3.0]\n' +
'[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# You are given an array of variable pairs equations and an array of real
# numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
# equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
# single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the
# j^th query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined,
# return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries
# will not result in division by zero and that there is no contradiction.
#
#
# Example 1:
#
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
#
#
# Example 2:
#
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
#
#
# Example 3:
#
#
# Input: equations = [["a","b"]], values = [0.5], queries =
# [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#
#
#
# Constraints:
#
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.
#
#
#

# @lc code=start


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # DFS

        # dists = {}
        # for (den, num), dist in zip(equations, values):
        #     if den not in dists:
        #         dists[den] = {}
        #     if num not in dists:
        #         dists[num] = {}
        #     dists[den][num] = dist
        #     dists[num][den] = 1 / dist
        # ans = []

        # def dfs(den, num, dists, visited):
        #     if den == num:
        #         return 1
        #     visited.add(den)
        #     for mid in dists[den]:
        #         if mid not in visited:
        #             midovernum = dfs(mid, num, dists, visited)
        #             if midovernum > 0:
        #                 return dists[den][mid] * midovernum
        #     return -1

        # for den, num in queries:
        #     if (den not in dists) or (num not in dists):
        #         ans.append(-1)
        #     else:
        #         visited = set()
        #         ans.append(dfs(den, num, dists, visited))
        # return ans

        # Union Find
        def find(x):  # return (parent, ratio over parent)
            if x != U[x][0]:
                px, pv = find(U[x][0])
                U[x] = px, U[x][1] * pv  # update to common parent and ratio
            return U[x]

        def divide(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry:
                return -1
            return vx / vy

        U = {}  # key, value; value = (parent, key/parent)
        for (den, num), ratio in zip(equations, values):
            if den not in U and num not in U:
                U[den] = (num, ratio)
                U[num] = (num, 1)
            elif den not in U:  # num in U
                U[den] = (num, ratio)
            elif num not in U:  # den in U
                U[num] = (den, 1 / ratio)
            else:
                parentofden, denoverp = find(den)
                parentofnum, numoverp = find(num)
                U[parentofden] = (parentofnum, ratio * numoverp / denoverp)

        ans = []
        for x, y in queries:
            if x in U and y in U:
                ans.append(divide(x, y))
            else:
                ans.append(-1)
        return ans

# @lc code=end
