# https://leetcode.com/problems/unique-binary-search-trees/
# 96. Unique Binary Search Trees
# Medium
#
# 2646
#
# 98
#
# Add to List
#
# Share
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# Accepted
# 255,594
# Submissions
# 511,804


# %% Dynamical Programming
# https://www.youtube.com/watch?v=HWJEMKWzy-Q

class Solution:
    def numTrees(self, n: int) -> int:
        if n < 1:
            return 0
        res = [0] * (n + 1)  # res[0] is for special case, res[n] is result
        res[0], res[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(0, i):
                res[i] = res[i] + res[j] * res[i - 1 - j]
        return res[n]


# %%
Solution().numTrees(3)
