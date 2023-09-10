#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (39.32%)
# Likes:    8955
# Dislikes: 643
# Total Accepted:    829.4K
# Total Submissions: 2.1M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
#
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
#
#
#


# %%
# @lc code=start
class Solution:
    def merge(self, intervals_sorted: list[list[int]]) -> list[list[int]]:
        # merge sorted intervals (from leetcode #56)
        ans = []
        for interval in intervals_sorted:
            if (not ans) or (interval[0] > ans[-1][1]):
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans

    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        # insert and merge
        if len(intervals) == 0:
            return [newInterval]
        # insert new interval into the pre-ordered list
        inserted = []
        i = 0
        while (i < len(intervals)) and (intervals[i][0] <= newInterval[0]):
            inserted.append(intervals[i])
            i = i + 1
        inserted.append(newInterval)
        if i < len(intervals):
            inserted.extend(intervals[i:])
        # call merge function
        merged = self.merge(inserted)
        return merged


# @lc code=end
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

# intervals = [[1, 5]]
# newInterval = [2, 7]

solution = Solution()
print(solution.insert(intervals, newInterval))

# %%
