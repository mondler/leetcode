// 796. Rotate String
// Easy
//
// 1147
//
// 67
//
// Add to List
//
// Share
// We are given two strings, s and goal.
//
// A shift on s consists of taking string s and moving the leftmost character to the rightmost position. For example, if s = 'abcde', then it will be 'bcdea' after one shift on s. Return true if and only if s can become goal after some number of shifts on s.
//
// Example 1:
// Input: s = 'abcde', goal = 'cdeab'
// Output: true
//
// Example 2:
// Input: s = 'abcde', goal = 'abced'
// Output: false
// Note:
//
// s and goal will have length at most 100.
// Accepted
// 102,476
// Submissions
// 209,264


#include <iostream>
// #include <algorithm>    // std::sort
// #include <vector>       // std::vector
#include <string>
// #include <unordered_map>

using namespace std;

class Solution {
public:
bool rotateString(string s, string goal) {
        if (s.size() != goal.size()) {
                return false;
        }

        if ((s.size() == 0) & (goal.size() == 0)) {
                return true;
        }

        int nGoal = goal.size();

        for (int i = 0; i < nGoal; ++i) {
                // find matching char from goal and s[0]
                if (s[0] == goal[i]) {
                        int j = 0;
                        // check if whole sting matches from s to goal[i:]
                        while (j < nGoal) {
                                if (s[j] != goal[(i + j) % nGoal]) {
                                        break;
                                }
                                ++j;
                        }
                        if (j == s.size()) {
                                return true;
                        }
                }
        }

        return false;
}
};

int main() {
        string s = "abca";
        string goal = "bcab";
        auto foo = Solution();
        cout << foo.rotateString(s, goal) << endl;
        // cout << s.size() << endl;
        return 0;
}
