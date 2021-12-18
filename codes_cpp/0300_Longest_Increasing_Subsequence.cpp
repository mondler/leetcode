// 300. Longest Increasing Subsequence
// Medium
//
// 7284
//
// 162
//
// Add to List
//
// Share
// Given an integer array nums, return the length of the longest strictly increasing subsequence.
//
// A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
//
//
//
// Example 1:
//
// Input: nums = [10,9,2,5,3,7,101,18]
// Output: 4
// Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
// Example 2:
//
// Input: nums = [0,1,0,3,2,3]
// Output: 4
// Example 3:
//
// Input: nums = [7,7,7,7,7,7,7]
// Output: 1
//
//
// Constraints:
//
// 1 <= nums.length <= 2500
// -104 <= nums[i] <= 104
//
//
// Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
//
// Accepted
// 550,941
// Submissions
// 1,224,884

#include <iostream>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
// #include <string>
// #include <unordered_map>

using namespace std;

class Solution {
public:

void printvec(vector<int> v) {
        for (auto n: v) {
                cout << n << endl;
        }
        return;
}

int max(int a, int b) {
        return (a<b)?b:a;
}

int lengthOfLIS(vector<int>& nums) {
        // https://leetcode.com/problems/longest-increasing-subsequence/discuss/74848/9-lines-C%2B%2B-code-with-O(NlogN)-complexity
        vector<int> res;
        for(int i=0; i<nums.size(); i++) {
                auto it = std::lower_bound(res.begin(), res.end(), nums[i]);
                if(it==res.end()) res.push_back(nums[i]);
                else *it = nums[i];
        }
        return res.size();
}

int lengthOfLIS2(vector<int>& nums) {
        // https://www.geekxh.com/1.2.动态规划系列/203.html#_01、题目分析
        if (nums.size() == 1) {
                return 1;
        }

        int maxLIS = 1;

        // currLIS records maxLIS ending with each element in nums
        vector<int> currLIS(nums.size(), 1);

        // iterate over each element to update currLIS
        for (int i = 1; i < nums.size(); ++i) {
                for (int j = 0; j < i; ++j) {
                        if (nums[j] < nums[i]) {
                                currLIS[i] = max(currLIS[i], currLIS[j] + 1);
                        }
                }

                // update result if get a bigger length
                maxLIS = max(maxLIS, currLIS[i]);
        }

        return maxLIS;
}
};


int main() {
        Solution foo = Solution();

        vector<int> nums = {0,1,0,3,2,3};
        cout << foo.lengthOfLIS(nums);
        cout << foo.lengthOfLIS2(nums);
        nums = {10,9,2,5,3,7,101,18};
        cout << foo.lengthOfLIS(nums);
        cout << foo.lengthOfLIS2(nums);
        nums = {2, 2, 2};
        cout << foo.lengthOfLIS(nums);
        cout << foo.lengthOfLIS2(nums);

        // cout << *max_element(nums.begin(), nums.end());

        // vector<int> res = foo.lis(nums);
        //
        // for (auto n: res) {
        //         cout << n << endl;
        // }

        // int mid = nums.size() / 2;
        //
        // vector<int> left(nums.begin(), nums.begin() + mid);
        // foo.printvec(left);


        // cout << foo.lengthOfLIS(nums) << endl;

        // int mid = nums.size() / 2;
        //
        //
        // vector<int> left(nums.begin(), nums.begin() + mid);
        // vector<int> right(nums.begin() + mid, nums.end());
        //
        // for (auto n: left) {
        //         cout << n << endl;
        // }
        //
        // cout << endl;
        //
        // for (auto n: right) {
        //         cout << n << endl;
        // }

        // vector<int> left = {0, 2, 4, 9, 10};
        // vector<int> right = {8, 12};
        // vector<int> rightjoin = foo.crossLIS(left, right);
        // for (auto n: rightjoin) {
        //         cout << n << endl;
        // }
        return 0;
}
