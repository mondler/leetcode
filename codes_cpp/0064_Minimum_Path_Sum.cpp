// 64. Minimum Path Sum
// Medium
//
// 4794
//
// 86
//
// Add to List
//
// Share
// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
//
// Note: You can only move either down or right at any point in time.
//
//
//
// Example 1:
//
//
// Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
// Output: 7
// Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
// Example 2:
//
// Input: grid = [[1,2,3],[4,5,6]]
// Output: 12
//
//
// Constraints:
//
// m == grid.length
// n == grid[i].length
// 1 <= m, n <= 200
// 0 <= grid[i][j] <= 100
// Accepted
// 545,036
// Submissions
// 958,742




#include <iostream>
// #include <algorithm>    // std::sort
#include <vector>       // std::vector
// #include <string>
// #include <unordered_map>

using namespace std;


class Solution {
public:
void printvec(vector<int> v) {
        for (auto n: v) {
                cout << n << " ";
        }
        cout << endl;
        return;
}

void printvecvec(vector<vector<int> >& grid) {
        for (auto row: grid) {
                printvec(row);
        }
        return;
}

int minPathSum(vector<vector<int> >& grid) {
        // # of row
        int m = grid.size();
        // # of col
        int n = grid[0].size();
        // cout << m << " " << n << endl;

        // initialize matrix to save shortest path to each element
        // vector<vector<int> > path(m, vector<int>(n));
        // printvecvec(path);
        // cout << endl;

        // first column
        for (int i = 0; i < m; ++i) {
                if (i == 0) {
                        grid[i][0] = grid[0][0];
                }
                else {
                        grid[i][0] = grid[i-1][0] + grid[i][0];
                }
        }

        // first row
        for (int j=1; j < n; ++j) {
                grid[0][j] = grid[0][j-1] + grid[0][j];
        }

        // each row afterwards
        for (int i = 1; i < m; ++i) {
                for (int j = 1; j < n; ++j) {
                        grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j];
                }
        }

        // printvecvec(path);
        // cout << endl;

        return grid[m-1][n-1];
}
};

int main() {
        vector<vector<int> > grid = {{1, 3, 1},{1,5,1},{4, 2, 1}};
        Solution foo = Solution();
        foo.printvecvec(grid);
        cout << endl;
        cout << foo.minPathSum(grid) << endl;
        // foo.printvecvec(grid);
        return 0;
}
