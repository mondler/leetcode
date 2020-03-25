# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
# 95. Unique Binary Search Trees II
# Medium
#
# 1797
#
# 146
#
# Add to List
#
# Share
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# Accepted
# 174,022
# Submissions
# 448,654


# %% divide and conquer
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int):
        def buildSubTree(left, right):
            if left > right:
                return [None]
            res = []
            for curr_root in range(left, right + 1):
                leftTree = buildSubTree(left, curr_root - 1)
                rightTree = buildSubTree(curr_root + 1, right)

                for l in leftTree:
                    for r in rightTree:
                        root = TreeNode(curr_root)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        if n == 0:
            return []
        return buildSubTree(1, n)


# %%
Solution().generateTrees(3)
