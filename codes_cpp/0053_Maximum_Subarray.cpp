// 53. Maximum Subarray
// Easy
//
// 12074
//
// 582
//
// Add to List
//
// Share
// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
//
//
//
// Example 1:
//
// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.
// Example 2:
//
// Input: nums = [1]
// Output: 1
// Example 3:
//
// Input: nums = [5,4,-1,7,8]
// Output: 23
//
//
// Constraints:
//
// 1 <= nums.length <= 3 * 104
// -105 <= nums[i] <= 105
//
//
// Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
// Accepted
// 1,436,131
// Submissions
// 2,989,997

#include <iostream>
// #include <algorithm>    // std::sort
#include <vector>       // std::vector
// #include <string>
// #include <unordered_map>

using namespace std;


class Solution {
public:
int maxSubArray(vector<int>& nums) {
        // int n = nums.size();
        int res = nums[0];

        // to save: max sum up to and with index i
        vector<int> maxSumWithN(n, 0);
        maxSumWithN[0] = res;
        for (int i=1; i < nums.size(); ++i) {
                if (maxSumWithN[i - 1] < 0) {
                        maxSumWithN[i] = nums[i];
                }
                else {
                        maxSumWithN[i] = maxSumWithN[i - 1] + nums[i];
                }
                if (maxSumWithN[i] > res) {
                        res = maxSumWithN[i];
                }
        }
        return res;
}

int maxSubArray2(vector<int>& nums) {
        // int n = nums.size();
        int res = nums[0];

        // to save: max sum up to and with index i
        int maxEndingHere = res;

        for (int i=1; i < nums.size(); ++i) {
                if (maxEndingHere < 0) {
                        maxEndingHere = nums[i];
                }
                else {
                        maxEndingHere = maxEndingHere + nums[i];
                }
                if (maxEndingHere > res) {
                        res = maxEndingHere;
                }
        }
        return res;
}
};


int main() {
        vector<int> nums = {4,-1,2,1};
        Solution foo = Solution();
        cout << foo.maxSubArray(nums) << endl;
        cout << foo.maxSubArray2(nums) << endl;
        // cout << nums[1] << endl;
        return 0;
}
