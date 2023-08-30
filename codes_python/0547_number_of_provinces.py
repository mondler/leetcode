#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
# https://leetcode.com/problems/number-of-provinces/description/
#
# algorithms
# Medium (62.73%)
# Likes:    5989
# Dislikes: 258
# Total Accepted:    522.3K
# Total Submissions: 828.5K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# There are n cities. Some of them are connected, while some are not. If city a
# is connected directly with city b, and city b is connected directly with city
# c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# i^th city and the j^th city are directly connected, and isConnected[i][j] = 0
# otherwise.
#
# Return the total number of provinces.
#
#
# Example 1:
#
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
#
#
# Example 2:
#
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
#
#
#

# @lc code=start


class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n + 1)]
        self._ranks = [1 for i in range(n + 1)]

    def find(self, u):
        if u != self._parents[u]:
            # path compression, modify parent of u to be its grandparent, save time for next run
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            # no union needed; already same group
            return False
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        return True


class Solution:
    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        # DFS: find all connected friends, modify isConnected from 1 to 0
        def DFS(isConnected, r, n):
            for c in range(n):
                if isConnected[r][c] == 1:
                    isConnected[r][c] = 0
                    isConnected[c][r] = 0
                    DFS(isConnected, c, n)
            return
        n = len(isConnected)
        if n == 0:
            return 0
        ans = 0
        for r in range(n):
            if isConnected[r][r] == 1:
                ans += 1
                DFS(isConnected, r, n)
        return ans

    def findCircleNum(self, isConnected):
        # union find set
        n = len(isConnected)
        if n == 0:
            return 0
        u = UnionFindSet(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    u.union(i, j)
        circles = set()
        for i in range(n):
            circles.add(u.find(i))

        return len(circles)
# @lc code=end
