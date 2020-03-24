# https://leetcode.com/problems/validate-binary-search-tree/
# 98. Validate Binary Search Tree
# Medium
#
# 3220
#
# 458
#
# Add to List
#
# Share
# Given a binary tree, determine if it is a valid binary search tree(BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# Accepted
# 601,578
# Submissions
# 2,212,734

# %%


def add(x: float, y: float) -> float:
    return x + y


add(3, 4)

# %% divide and couquer

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidNode(node: TreeNode, lower, upper) -> bool:
            if not(node):
                return True
            if (upper is not None) and (node.val >= upper):
                return False
            if (lower is not None) and (node.val <= lower):
                return False
            validate_left = isValidNode(node.left, lower, node.val)
            validate_right = isValidNode(node.right, node.val, upper)
            return (validate_left and validate_right)
        return isValidNode(root, None, None)


# %% in order search all nodes, and evaluate values

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not(root):
            return True
        storage = []
        self.inOrder(root, storage)
        for i in range(1, len(storage)):
            if storage[i] <= storage[i - 1]:
                return False
        return True

    # store nodes in binary search tree from low to high (left to right)
    def inOrder(self, root, storage):
        if root is None:
            return
        self.inOrder(root.left, storage)
        storage.append(root.val)
        self.inOrder(root.right, storage)

# %% evaluate during in order search of all nodes; best in this case


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = None

        def inOrder(root):
            # assign nonlocal so that its value is changed properly
            nonlocal prev
            # search nodes in binary search tree from low to high
            if not(root):
                return True
            if not(inOrder(root.left)):
                # if rank order breaks on left tree, return False immediately
                return False
            if (prev is not None) and (root.val <= prev):
                # return false when rank order breaks
                return False
            prev = root.val
            return inOrder(root.right)
        return inOrder(root)



# %% test cases
a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)
a.left = b
a.right = c


Solution().isValidBST(a)


# %%
class test:
    def test(self) -> bool:
        prev = 2

        def inOrder():
            if prev is None:
                print("TRUE")
            print(prev)
        inOrder()


test().test()
