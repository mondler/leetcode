#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (45.32%)
# Likes:    8267
# Dislikes: 285
# Total Accepted:    856.7K
# Total Submissions: 1.9M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#

# @lc code=start
# from calendar import c


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # treat 2D array as 1D array
        r, c = len(matrix), len(matrix[0])
        low, high = 0, r * c - 1
        while low <= high:
            mid = low + (high - low) // 2
            m, n = mid // c, mid % c
            num = matrix[m][n]
            if num == target:
                return True
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


# @lc code=end

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 5

print(Solution().searchMatrix(matrix, target))
