# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# 435. Non-overlapping Intervals
# Medium
#
# 782
#
# 28
#
# Add to List
#
# Share
# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
#
#
# Example 1:
#
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
#
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
#
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
#
#
# Note:
#
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
# Accepted
# 58,970
# Submissions
# 139,649


# %% count maximum number of intervals to keep
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda a: a[1])  # sort all by end point
        count = 1  # automatically include the first one
        i = 1
        curr_st, curr_end = intervals[0]
        # for interval in intervals[1:]:
        #     if (interval[0] >= curr_end):
        #         count += 1
        #         curr_st, curr_end = interval
        while i < n:
            next_start = intervals[i][0]
            if (curr_st < next_start >= curr_end):
                count += 1
                curr_st = next_start
                curr_end = intervals[i][1]
            i += 1
        return n - count


# %% count number of intervals to remove
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda a: (a[1], a[0]))  # sort all by end point
        count = 0  # count of interval to be removed
        curr_st, curr_end = intervals[0]
        for i in range(1, n):
            next_start = intervals[i][0]
            if next_start < curr_end:  # if next item's start lower than previous end
                count += 1
            else:
                curr_st, curr_end = intervals[i]
        return count


# %%
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
Solution().eraseOverlapIntervals(intervals)

intervals = [[1, 2], [1, 2], [1, 2]]
Solution().eraseOverlapIntervals(intervals)

intervals = [[1, 2], [2, 3]]
Solution().eraseOverlapIntervals(intervals)

intervals = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
Solution().eraseOverlapIntervals(intervals)
