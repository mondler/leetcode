// 125. Valid Palindrome
// Easy
//
// 2044
//
// 3897
//
// Add to List
//
// Share
// Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
//
//
//
// Example 1:
//
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
// Example 2:
//
// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.
//
//
// Constraints:
//
// 1 <= s.length <= 2 * 105
// s consists only of printable ASCII characters.
// Accepted
// 876,753
// Submissions
// 2,253,412

#include <iostream>
// #include <algorithm>    // std::sort
// #include <vector>       // std::vector
#include <string>
// #include <unordered_map>

using namespace std;

class Solution {
public:
bool isPalindrome(string s) {

        for (int left = 0, right = s.size() - 1; left < right; ++left, --right) {
                while ((left < right) && (isalnum(s[left]) == 0)) {
                        ++left;
                }
                while ((left < right) && (isalnum(s[right]) == 0)) {
                        --right;
                }
                if (left < right) {
                        if (tolower(s[left]) != tolower(s[right])) {
                                return false;
                        }

                }
        }
        return true;
}

bool isPalindrome2(string s) {
        int left = 0;
        int right = s.size() - 1;
        while (left < right) {
                while ((left < right) && (isalnum(s[left]) == 0)) {
                        ++left;
                }
                while ((left < right) && (isalnum(s[right]) == 0)) {
                        --right;
                }
                if (left < right) {
                        if (tolower(s[left]) != tolower(s[right])) {
                                return false;
                        }
                        else {
                                ++left;
                                --right;
                        }
                }
                else {
                        break;
                }
        }
        return true;
}
};

int main() {
        string s = "0P";
        auto foo = Solution();
        cout << foo.isPalindrome(s) << endl;
        // for (auto c: s) {
        //         cout << isalpha(c) << endl;
        // }

        return 0;
}
