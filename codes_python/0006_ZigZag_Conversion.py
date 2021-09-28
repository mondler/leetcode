# 6. ZigZag Conversion
# Medium
#
# 2362
#
# 5830
#
# Add to List
#
# Share
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1) or (numRows > len(s)):
            return s
        rows = [''] * numRows

        row = 0
        increment = 1

        for c in s:
            rows[row] += c
            row += increment
            if (row == (numRows - 1)) or (row == 0):
                increment *= -1

        return ''.join(rows)

    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for i in range(numRows)]
        n = len(s)
        for i in range(n):
            j = i % (2 * numRows - 2)
            if j < numRows:
                rows[j].append(s[i])
            else:
                rows[2 * numRows - 2 - j].append(s[i])

        sNew = [row[i] for row in rows for i in range(len(row))]

        return ''.join(sNew)


# s = "PAYPALISHIRING"
s = "ABCDEFG"
numRows = 3

Solution().convert(s, numRows)
