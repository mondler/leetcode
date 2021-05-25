# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# 452. Minimum Number of Arrows to Burst Balloons
# Medium
#
# 706
#
# 38
#
# Add to List
#
# Share
# There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.
#
# An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.
#
# Example:
#
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
#
# Output:
# 2
#
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
#
#
# Accepted
# 53,441
# Submissions
# 110,902


# %%
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 1:
            return n
        points.sort(key=lambda a: a[1])  # sort by endpoint
        count = 1
        curr_st, curr_end = points[0]
        for i in range(1, n):
            next_st = points[i][0]
            if next_st > curr_end:
                count += 1
                curr_st, curr_end = next_st, points[i][1]
        return count


# %%
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
Solution().findMinArrowShots(points)
