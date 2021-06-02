// 344. Reverse String
// Easy
//
// 2459
//
// 779
//
// Add to List
//
// Share
// Write a function that reverses a string. The input string is given as an array of characters s.
//
//
//
// Example 1:
//
// Input: s = ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]
// Example 2:
//
// Input: s = ["H","a","n","n","a","h"]
// Output: ["h","a","n","n","a","H"]
//
//
// Constraints:
//
// 1 <= s.length <= 105
// s[i] is a printable ascii character.
//
//
// Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
//
// Accepted
// 1,057,383
// Submissions
// 1,487,296

#include <iostream>
// #include <algorithm>    // std::sort
#include <vector>       // std::vector
// #include <string>
// #include <unordered_map>

using namespace std;

class Solution {
public:
void printvec(vector<char>& v) {
        for (auto n: v) {
                cout << n << " ";
        }
        cout << endl;
        return;
}

void swap(char& c1, char& c2) {
        char temp;
        temp = c1;
        c1 = c2;
        c2 = temp;
}

void reverseString(vector<char>& s) {
        // printvec(s);
        int left, right;
        left = 0;
        right = s.size() - 1;
        while (left < right) {
                swap(s[left++], s[right--]);
                // ++left;
                // --right;
        }
        // cout << s[s.size() - 1];
        return;
}
};

int main() {
        vector<char> s = {'a', 'b', 'c'};
        auto foo = Solution();
        foo.reverseString(s);
        foo.printvec(s);
        return 0;
}
