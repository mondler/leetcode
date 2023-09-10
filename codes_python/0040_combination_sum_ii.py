#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (53.69%)
# Likes:    9502
# Dislikes: 238
# Total Accepted:    814.1K
# Total Submissions: 1.5M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# Constraints:
#
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
#
#


# @lc code=start
class Solution:
    def combinationSum2(
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        candidates.sort()
        res = []  # list of vectors adding to target
        self.dfs(candidates, target, 0, res, [])
        return res

    def dfs(self, candidates, target, l, res, cur):
        # print(target, l, cur)
        if target == 0:
            res.append(cur.copy())
            return

        for i in range(l, len(candidates)):
            # beloe condition is to avoid duplicate answers
            # [1, 1, 1, 5] 7  would not consider the last 1
            if (i > l) and (candidates[i] == candidates[i - 1]):
                continue
            if candidates[i] > target:
                return
            cur.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i + 1, res, cur)
            cur.pop()
        return


# @lc code=end

solution = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(solution.combinationSum2(candidates, target))
