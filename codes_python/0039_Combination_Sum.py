# 39. Combination Sum
# Medium
#
# 7642
#
# 183
#
# Add to List
#
# Share
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
#
#
#
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
#
# Input: candidates = [2], target = 1
# Output: []
# Example 4:
#
# Input: candidates = [1], target = 1
# Output: [[1]]
# Example 5:
#
# Input: candidates = [1], target = 2
# Output: [[1,1]]
#
#
# Constraints:
#
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500
# Accepted
# 851,687
# Submissions
# 1,367,787
# %%
class Solution:
    def combinationSum(
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        candidates.sort()
        res = []  # list of vectors adding to target
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, l, cur, res):
        if target == 0:
            res.append(cur.copy())
            return

        for i in range(l, len(candidates)):
            if candidates[i] > target:
                return
            cur.append(candidates[i])
            # print(f"{cur=}")
            # print(f"{res=}")
            self.dfs(candidates, target - candidates[i], i, cur, res)
            cur.pop()
        return


candidates = [2, 3, 6, 7]
target = 7

# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8

print(Solution().combinationSum(candidates, target))
