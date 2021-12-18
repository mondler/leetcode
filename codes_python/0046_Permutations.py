# https://leetcode.com/problems/permutations/description/
# Medium
#
# 3384
#
# 98
#
# Add to List
#
# Share
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
# Accepted
# 553,864
# Submissions
# 901,471

# %% DFS + Implicit Backtracking  ~40ms


class Solution(object):
    def permute(self, nums):
        res = []
        n = len(nums)
        self.dfs(nums, [], res, n)
        return res

    def dfs(self, nums, path, res, n):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(n):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res, n - 1)


# %% DFS + Backtracking  ~44ms


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)

        def DFS(item, idx):
            # idx: fill in the idx-th element
            if idx == n:
                ans.append(item)
                return

            for i in range(n - idx):
                elem = nums[i]
                item.append(elem)
                nums.pop(i)
                DFS(item, idx + 1)
                nums.insert(i, elem)
                item = item[:idx]

        DFS([], 0)

        return ans


# %%
nums = [1, 2, 3]
Solution().permute(nums)
