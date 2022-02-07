// 198. House Robber
// Medium
//
// 7177
//
// 198
//
// Add to List
//
// Share
// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
//
// Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
//
//
//
// Example 1:
//
// Input: nums = [1,2,3,1]
// Output: 4
// Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
// Total amount you can rob = 1 + 3 = 4.
// Example 2:
//
// Input: nums = [2,7,9,3,1]
// Output: 12
// Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
// Total amount you can rob = 2 + 9 + 1 = 12.
//
//
// Constraints:
//
// 1 <= nums.length <= 100
// 0 <= nums[i] <= 400
// Accepted
// 727,377
// Submissions
// 1,674,394

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

int robHelper(vector<int>& nums, int idx) {
        // max sum ending with idx-th element in nums

        // int m = nums.size();
        // vector<int> totalHere(m, 0);
        if (idx <= 1) {
                return nums[idx];
        }
        if (idx == 2) {
                return nums[0] + nums[2];
        }
        // vector<int> totalHere(m, 0);

        // return max(robHelper(nums, idx-3), robHelper(nums, idx-2)) + nums[idx];
        return 0;
}

int rob(vector<int>& nums) {
        int rob(vector<int>& nums) {
                // int m = nums.size();
                if (nums.size() == 1) {
                        return nums[0];
                }
                if (nums.size() == 2) {
                        return max(nums[0], nums[1]);
                }

                int maxTillNow, maxLeft, maxLeftLeft;

                maxLeftLeft = nums[0];
                maxLeft = max(nums[0], nums[1]);

                for (int i = 2; i < nums.size(); ++i) {
                        maxTillNow = max(maxLeftLeft + nums[i], maxLeft);

                        maxLeftLeft = maxLeft;
                        maxLeft = maxTillNow;
                }

                return maxTillNow;
        }
}


int rob2(vector<int>& nums) {
        int m = nums.size();
        if (m == 1) {
                return robHelper(nums, 0);
        }
        if (m == 2) {
                return max(robHelper(nums, 0), robHelper(nums, 1));
        }
        if (m == 3) {
                return max(robHelper(nums, 1), robHelper(nums, 2));
        }

        vector<int> totalHere(m, 0);

        for (int i = 0; i < 3; ++i) {
                totalHere[i] = robHelper(nums, i);
        }
        for (int i = 3; i < m; ++i) {
                totalHere[i] = max(totalHere[i-3], totalHere[i-2]) + nums[i];
        }

        // printvec(totalHere);
        return max(totalHere[m-1], totalHere[m-2]);
}
};

int main() {
        vector<int> nums = {2, 7, 9, 3, 1};
        auto foo = Solution();
        cout << foo.rob(nums) << endl;
        cout << foo.rob2(nums) << endl;
        return 0;
}
