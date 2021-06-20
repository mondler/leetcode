// Easy
//
// 1147
//
// 3244
//
// Add to List
//
// Share
// Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
//
// A word is a maximal substring consisting of non-space characters only.
//
//
//
// Example 1:
//
// Input: s = "Hello World"
// Output: 5
// Example 2:
//
// Input: s = " "
// Output: 0
//
//
// Constraints:
//
// 1 <= s.length <= 104
// s consists of only English letters and spaces ' '.
// Accepted
// 515,211
// Submissions
// 1,532,968

#include <iostream>
// #include <algorithm>    // std::sort
// #include <vector>       // std::vector
#include <string>
// #include <unordered_map>

using namespace std;

class Solution {
public:
int lengthOfLastWord(string s) {
        if (s.size() == 0) {
                return 0;
        }
        int i = s.size() - 1;
        int res = 0;
        while (i >= 0) {
                if (isspace(s[i]) == false) {
                        break;
                }
                --i;
        }
        while (i >= 0) {
                if (isspace(s[i]) == false) {
                        ++res;
                        --i;
                }
                else {
                        break;
                }
        }
        return res;
}
};

int main() {
        string s = "abc";
        auto foo = Solution();
        cout << foo.lengthOfLastWord(s) << endl;
        return 0;
}
