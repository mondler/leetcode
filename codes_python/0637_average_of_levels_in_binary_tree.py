#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (69.00%)
# Likes:    3294
# Dislikes: 252
# Total Accepted:    293.6K
# Total Submissions: 423.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the average value of the nodes on
# each level in the form of an array. Answers within 10^-5 of the actual answer
# will be accepted.
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11.
# Hence return [3, 14.5, 11].
#
#
# Example 2:
#
#
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#

import collections

# @lc code=start
# Definition for a binary tree node.
import numpy as np


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels2(self, root: Optional[TreeNode]) -> list[float]:
        # BFS
        if root is None:
            return []
        # ans = [root.val]
        ans = []
        q = collections.deque([root])
        while q:
            s = len(q)
            temp = 0
            l = 0
            while s > 0:
                node = q.popleft()
                temp += node.val
                l += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                s -= 1
            ans.append(temp / l)
        return ans

    def averageOfLevels(self, root):
        if root is None:
            return []
        ans = []
        totals = []  # each element is a list [sum over this level, number of nodes this level]
        self.DFS(root, 0, totals)
        print(totals)
        for total in totals:
            ans.append(total[0] / total[1])
            # print(total[0] / total[1])
        return ans

    def DFS(self, root, depth, totals):
        if root is None:
            return
        if (depth >= len(totals)):
            totals.append([0, 0])
        totals[depth][0] += root.val
        totals[depth][1] += 1
        self.DFS(root.left, depth + 1, totals)
        self.DFS(root.right, depth + 1, totals)
        return

# @lc code=end
