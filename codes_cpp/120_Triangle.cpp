// 120. Triangle
// Medium
//
// 3169
//
// 325
//
// Add to List
//
// Share
// Given a triangle array, return the minimum path sum from top to bottom.
//
// For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
//
//
//
// Example 1:
//
// Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
// Output: 11
// Explanation: The triangle looks like:
//    2
//   3 4
//  6 5 7
// 4 1 8 3
// The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
// Example 2:
//
// Input: triangle = [[-10]]
// Output: -10
//
//
// Constraints:
//
// 1 <= triangle.length <= 200
// triangle[0].length == 1
// triangle[i].length == triangle[i - 1].length + 1
// -104 <= triangle[i][j] <= 104
//
//
// Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
// Accepted
// 318,085
// Submissions
// 674,556

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

int minimumTotal(vector<vector<int> >& triangle) {
        int s1 = triangle.size();
        if (s1==1) {
                return triangle[0][0];
        }
        vector<int> lastlayer(s1, 0);
        vector<int> currlayer(s1, 0);

        lastlayer[0] = triangle[0][0];
        // update shortest path to i-th row
        for (int i=1; i < s1; ++i) {
                // shorttest path to j-th element in this row

                // left and right
                currlayer[0] = lastlayer[0] + triangle[i][0];
                currlayer[i] = lastlayer[i-1] + triangle[i][i];

                // middle
                for (int j = 1; j < i; ++j) {
                        currlayer[j] = min(lastlayer[j-1], lastlayer[j]) + triangle[i][j];
                }

                // assign currlayer to lastlayer

                for (int k = 0; k < i + 1; ++k) {
                        lastlayer[k] = currlayer[k];
                }

                // printvec(lastlayer);
        }
        // printvec(lastlayer);

        // int re


        return *min_element(lastlayer.begin(), lastlayer.end());;
}
};


int main() {
        vector<vector<int> > triangle = {{2},{3,4},{6,5,7},{4,1,8,3}};
        vector<vector<int> > triangle2 = {{2}};
        Solution foo = Solution();
        cout << foo.minimumTotal(triangle) << endl;
        cout << foo.minimumTotal(triangle2) << endl;
        // cout << *min_element(triangle[3].begin(), triangle[3].end());
        // cout << foo.minimumTotal(triangle2) << endl;
        // cout << min(foo.minimumTotal(triangle), foo.minimumTotal(triangle2)) << endl;
        return 0;
}
