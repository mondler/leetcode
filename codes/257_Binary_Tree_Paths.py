# https://leetcode.com/problems/binary-tree-paths/description/
# 257. Binary Tree Paths
# Easy
#
# 1443
#
# 90
#
# Add to List
#
# Share
# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# %% DFS + implicit backtracking ~28ms
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []

        def DFS(current_root, path):
            if current_root is None:
                return

            if current_root.left is None and current_root.right is None:
                temp = path + [str(current_root.val)]
                ans.append('->'.join(temp))
                return

            DFS(current_root.left, path + [str(current_root.val)])
            DFS(current_root.right, path + [str(current_root.val)])

        DFS(root, [])

        return ans


# %%
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node5 = TreeNode(5)

node1.left = node2
node2.right = node5
node1.right = node3

root = node1

Solution().binaryTreePaths(root)
