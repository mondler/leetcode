// Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
//
// The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
//
// You may assume the integer does not contain any leading zero, except the number 0 itself.
//
// Example 1:
//
// Input: [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Example 2:
//
// Input: [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.

#include <iostream>
#include <vector>
#include <string>
using namespace std;

//
class Solution {
public:
void reverse(vector<int>& nums, int start, int end) {
        // reverse subvector from location start to end
        int count = 0;     // current number of switches
        // int i = start;
        // int s = nums.size();
        int s = end - start + 1;
        int m = s / 2;     // total number of switches
        // switch m mtimes to reverse
        while (count < m) {
                swap(nums[start + count], nums[end - count]);
                count++;
        }
        return;
}

vector<int> plusOne(vector<int>& digits) {

        // reverse
        int s = digits.size();
        // reverse(digits, 0, s - 1);

        int i = s - 1;
        while (i >= 0) {
                if (digits[i] == 9) {
                        digits[i] = 0;
                        i--;
                }
                else {
                        digits[i] += 1;
                        break;
                }
        }
        if (i == -1) {
                digits.insert(digits.begin(), 1);
        }

        return digits;

}

vector<int> plusOne2(vector<int>& digits) {

        // reverse
        int s = digits.size();
        reverse(digits, 0, s - 1);

        int i = 0;
        while (i < s) {
                if (digits[i] == 9) {
                        digits[i] = 0;
                        i++;
                }
                else {
                        digits[i] += 1;
                        break;
                }
        }

        // if every digits need to be modified (eg: 99)
        if (i == s) {
                digits.push_back(1);
        }

        // reverse back
        reverse(digits, 0, digits.size() - 1);

        return digits;

}
};

//
int main() {
        std::vector<int> nums = {9, 9, 9};
        // int val = 2;

        Solution foo = Solution();
        vector<int> numsplusone = foo.plusOne(nums);

        for (const auto i: numsplusone)
                cout << i;

        return 0;
}
