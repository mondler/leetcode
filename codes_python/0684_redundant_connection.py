#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (61.48%)
# Likes:    4394
# Dislikes: 316
# Total Accepted:    231.7K
# Total Submissions: 374.8K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
#
# You are given a graph that started as a tree with n nodes labeled from 1 to
# n, with one additional edge added. The added edge has two different vertices
# chosen from 1 to n, and was not an edge that already existed. The graph is
# represented as an array edges of length n where edges[i] = [ai, bi] indicates
# that there is an edge between nodes ai and bi in the graph.
#
# Return an edge that can be removed so that the resulting graph is a tree of n
# nodes. If there are multiple answers, return the answer that occurs last in
# the input.
#
#
# Example 1:
#
#
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
#
#
# Example 2:
#
#
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
#
#
#
# Constraints:
#
#
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
#
#
#


# @lc code=start
class Solution:
    # union find
    #
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        p = [0]*(len(edges) + 1)
        s = [1]*(len(edges) + 1)

        def find(u):
            while p[u] != u:
                p[u] = p[p[u]]
                u = p[u]
            return u

        for u, v in edges:
            if p[u] == 0:  # add to union find
                p[u] = u
            if p[v] == 0:
                p[v] = v
            pu, pv = find(u), find(v)
            if pu == pv:  # if already in the same group
                return [u, v]

            if s[pv] > s[pu]:
                u, v = v, u
            p[pv] = pu
            s[pu] += s[pv]

        return []
# @lc code=end
