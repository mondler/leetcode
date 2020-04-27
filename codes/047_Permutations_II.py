# https://leetcode.com/problems/permutations-ii/description/
# 47. Permutations II
# Medium
#
# 1687
#
# 58
#
# Add to List
#
# Share
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
# Accepted
# 327,604
# Submissions
# 728,987

# %% DFS + Backtracking ~56ms


class Solution(object):
    def permuteUnique(self, nums):
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

            used = set()
            for i in range(n - idx):
                elem = nums[i]
                if elem in used:
                    continue
                used.add(elem)
                item.append(elem)
                nums.pop(i)
                DFS(item, idx + 1)
                nums.insert(i, elem)
                item = item[:idx]

        DFS([], 0)

        return ans


# %%
nums = [1, 1, 2]
Solution().permuteUnique(nums)
