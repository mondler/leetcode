#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#
# https://leetcode.com/problems/keys-and-rooms/description/
#
# algorithms
# Medium (69.49%)
# Likes:    3617
# Dislikes: 190
# Total Accepted:    225.7K
# Total Submissions: 322.9K
# Testcase Example:  '[[1],[2],[3],[]]'
#
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except
# for room 0. Your goal is to visit all the rooms. However, you cannot enter a
# locked room without having its key.
#
# When you visit a room, you may find a set of distinct keys in it. Each key
# has a number on it, denoting which room it unlocks, and you can take all of
# them with you to unlock the other rooms.
#
# Given an array rooms where rooms[i] is the set of keys that you can obtain if
# you visited room i, return true if you can visit all the rooms, or false
# otherwise.
#
#
# Example 1:
#
#
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation:
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
#
#
# Example 2:
#
#
# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks
# it is in that room.
#
#
#
# Constraints:
#
#
# n == rooms.length
# 2 <= n <= 1000
# 0 <= rooms[i].length <= 1000
# 1 <= sum(rooms[i].length) <= 3000
# 0 <= rooms[i][j] < n
# All the values of rooms[i] are unique.
#
#
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(keyss):
            for k in keyss:
                if k not in visited:
                    visited.add(k)
                    dfs(rooms[k])
            return

        def bfs(room):
            from collections import deque
            toVisit = deque({room})
            while toVisit:
                r = toVisit.popleft()
                if r not in visited:
                    visited.add(r)
                    for nextRoom in rooms[r]:
                        if nextRoom not in visited:
                            toVisit.append(nextRoom)
            return

        visited = set()
        # visited.add(0)
        nRooms = len(rooms)
        # dfs(rooms[0])
        bfs(0)
        # print(visited)
        return len(visited) == nRooms

# @lc code=end
