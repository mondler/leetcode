// 28. Implement strStr()
// Easy
//
// 2407
//
// 2438
//
// Add to List
//
// Share
// Implement strStr().
//
// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
//
// Clarification:
//
// What should we return when needle is an empty string? This is a great question to ask during an interview.
//
// For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
//
//
//
// Example 1:
//
// Input: haystack = "hello", needle = "ll"
// Output: 2
// Example 2:
//
// Input: haystack = "aaaaa", needle = "bba"
// Output: -1
// Example 3:
//
// Input: haystack = "", needle = ""
// Output: 0
//
//
// Constraints:
//
// 0 <= haystack.length, needle.length <= 5 * 104
// haystack and needle consist of only lower-case English characters.
// Accepted
// 893,615
// Submissions
// 2,514,111

#include <iostream>
// #include <algorithm>    // std::sort
// #include <vector>       // std::vector
#include <string>
// #include <unordered_map>

using namespace std;

class Solution {
public:

bool strMatch(string haystack, string needle, int idx) {
        // return if needle matches haystack starting from position idx
        int i = idx;
        int j = 0;
        while ((i < haystack.size()) && (j < needle.size())) {
                if (haystack[i] != needle[j]) {
                        return false;
                }
                ++i;
                ++j;
        }
        if (j == needle.size()) {
                return true;
        }
        return false;
}

int lastPosChar(string s, char c) {
        // return last occurence of char in string, -1 if not found
        int i = s.size() - 1;
        while (i >= 0) {
                if (s[i] == c) {
                        return i;
                }
                --i;
        }
        return -1;
}

int strStr(string haystack, string needle) {
        // Sunday String Match Method
        if (needle == "") {
                return 0;
        }
        int s = needle.size();
        int i = 0; // starting idx of haystack to check if matching needle
        char nextChar;
        while (i < haystack.size()) {
                // cout << i << endl << endl;

                if (strMatch(haystack, needle, i)) {
                        return i;
                }

                // go to the next char if no matching
                if (i + s < haystack.size()) {
                        nextChar = haystack[i + s];

                        // position of char in needle
                        int charPos = lastPosChar(needle, nextChar);

                        // set staring idx for next round of match
                        i = i + s - charPos;
                }
                else {
                        return -1;
                }
        }
        // if not found
        return -1;
}
};


int main() {
        string haystack = "aaaaa";
        string needle = "bba";
        char c = 'l';
        auto foo = Solution();
        // cout << haystack.size() << endl;
        cout << foo.strStr(haystack, needle) << endl;
        // cout << foo.strMatch(haystack, needle, 3) << endl;
        // cout << foo.lastPosChar(haystack, c) << endl;
        return 0;
}
