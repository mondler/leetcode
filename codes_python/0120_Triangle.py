# 120. Triangle
# Medium
#
# 3713
#
# 350
#
# Add to List
#
# Share
# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
#
#
#
# Example 1:
#
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:
#
# Input: triangle = [[-10]]
# Output: -10
#
#
# Constraints:
#
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104

# %%
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        h = len(triangle)
        if h == 1:
            return triangle[0][0]

        # lowest steps to each layer, initialization
        minToRow = [triangle[0][0]]

        for row in range(1, h):
            temp = [None] * (row + 1)
            for i in range(row + 1):
                upperLeft = i - 1
                if upperLeft >= 0:
                    temp[i] = minToRow[upperLeft] + triangle[row][i]
                upper = i
                if upper < row:
                    if temp[i] is None:
                        temp[i] = minToRow[upper] + triangle[row][i]
                    else:
                        temp[i] = min(
                            temp[i], minToRow[upper] + triangle[row][i])
            del minToRow
            minToRow = temp
        return min(minToRow)


# %%
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Solution().minimumTotal(triangle))

triangle = [[2]]
print(Solution().minimumTotal(triangle))
