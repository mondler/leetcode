# https://leetcode.com/problems/friend-circles/
# 547. Friend Circles
# Medium
#
# 1572
#
# 123
#
# Add to List
#
# Share
# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
#
# Example 1:
#
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:
#
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# Note:
#
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.
# Accepted
# 141,518
# Submissions
# 247,778


# %% DFS ~184ms created graph and visited to help
# https://zxi.mytechroad.com/blog/graph/leetcode-547-friend-circles/
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        N = len(M)

        import collections
        friend = collections.defaultdict(set)

        for p1 in range(N):
            for p2 in range(p1, N):
                if M[p1][p2] == 1:
                    friend[p1].add(p2)
                    friend[p2].add(p1)

        visited = [False] * N

        def dfs(p1):
            for p2 in friend[p1]:
                if visited[p2] == False:
                    visited[p2] = True
                    dfs(p2)

            return

        ans = 0
        # ok to search upper half of M
        for p1 in range(N):
            if visited[p1] == False:
                ans += 1
                dfs(p1)

        return ans


# %% DFS ~184ms
# https://zxi.mytechroad.com/blog/graph/leetcode-547-friend-circles/
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        N = len(M)

        # import collections
        # friend = collections.defaultdict(set)
        # for p1 in range(N):
        #     for p2 in range(p1, N):
        #         if M[p1][p2] == 1:
        #             friend[p1].add(p2)
        #             friend[p2].add(p1)

        visited = [False] * N

        def dfs(p1):
            for p2 in range(N):
                if visited[p2] == False and M[p1][p2] == 1:
                    visited[p2] = True
                    dfs(p2)
            return

        ans = 0
        # ok to search upper half of M
        for p1 in range(N):
            if visited[p1] == False:
                ans += 1
                dfs(p1)

        return ans


# %%
M = [[1, 0, 0, 1],
     [0, 1, 1, 0],
     [0, 1, 1, 1],
     [1, 0, 1, 1]]

Solution().findCircleNum(M)
