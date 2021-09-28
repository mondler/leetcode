// 387. First Unique Character in a String
// Easy
//
// 3031
//
// 147
//
// Add to List
//
// Share
// Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.
//
//
//
// Example 1:
//
// Input: s = "leetcode"
// Output: 0
// Example 2:
//
// Input: s = "loveleetcode"
// Output: 2
// Example 3:
//
// Input: s = "aabb"
// Output: -1
//
//
// Constraints:
//
// 1 <= s.length <= 105
// s consists of only lowercase English letters.
// Accepted
// 749,327
// Submissions
// 1,379,471

#include <iostream>
// #include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <string>
// #include <unordered_map>

using namespace std;

class Solution {
public:
int firstUniqChar(string s) {
        vector<int> ct(26, 0);
        for (auto c: s) {
                ct[c - 'a'] += 1;
        }
        for (int i = 0; i < s.size(); ++i) {
                if (ct[s[i] - 'a'] == 1) {
                        return i;
                }
        }

        return -1;
}
};

int main() {
        string s = "loveleetcode";
        // cout << s.size();
        auto foo = Solution();
        cout << foo.firstUniqChar(s);
        return 0;
}
