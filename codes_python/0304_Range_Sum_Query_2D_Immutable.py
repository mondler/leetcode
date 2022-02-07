# 304: Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/


# %%
# create cumSum for each position

# %%
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        nRow = len(matrix)
        nCol = len(matrix[0])
        dp = [[0] * nCol for i in range(nRow)]
        for r in range(nRow):
            for c in range(nCol):
                a = dp[r][c - 1] if c > 0 else 0
                b = dp[r - 1][c] if r > 0 else 0
                d = dp[r - 1][c - 1] if ((c > 0) and (r > 0)) else 0
                # if ((r == 0) and (c == 0)):
                dp[r][c] = a + b - d + matrix[r][c]
            # if r == 0:
            #     for c in range(nCol):
            #         dp[r][c] = dp[r][c - 1] + matrix[r][c]
            # else:
            #     for c in range(nCol):
            #         if c == 0:
            #             dp[r][c] = dp[r - 1][c] + matrix[r][c]
            #         else:
            #             dp[r][c] = dp[r][c - 1] + dp[r - 1][c] - \
            #                 dp[r - 1][c - 1] + matrix[r][c]

        self.dp = dp
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dp = self.dp

        a = dp[row2][col2]
        b = dp[row2][col1 - 1] if col1 > 0 else 0
        c = dp[row1 - 1][col2] if row1 > 0 else 0
        d = dp[row1 - 1][col1 - 1] if ((col1 > 0) and (row1 > 0)) else 0
        return a - b - c + d

        # if (row1 == 0) and (col1 == 0):
        #     return dp[row2][col2]
        # if row1 == 0:
        #     return dp[row2][col2] - dp[row2][col1 - 1]
        # if col1 == 0:
        #     return dp[row2][col2] - dp[]
        # return dp[row2][col2] - dp[row2][col1 - 1] - dp[row1 - 1][col2] + dp[row1 - 1][col1 - 1]

# %%
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


matrix = [[1, 1, 1],
          [1, 1, 1],
          ]


obj = NumMatrix(matrix)

obj.dp

print(obj.sumRegion(1, 0, 1, 1))


# %%
