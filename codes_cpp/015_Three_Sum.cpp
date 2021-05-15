// https://leetcode.com/problems/3sum/
// 15. 3Sum
// Medium
//
// 10434
//
// 1068
//
// Add to List
//
// Share
// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
//
// Notice that the solution set must not contain duplicate triplets.
//
//
//
// Example 1:
//
// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Example 2:
//
// Input: nums = []
// Output: []
// Example 3:
//
// Input: nums = [0]
// Output: []
//
//

//
// 0 <= nums.length <= 3000
// -105 <= nums[i] <= 105

#include <iostream>

#include <algorithm>    // std::sort
#include <vector>       // std::vector
// #include <string>
// #include <unordered_map>

using namespace std;

//
class Solution {
public:
vector<vector<int> > threeSum(vector<int>& nums) {
        vector<vector<int> > results;
        // vector<int> result;
        sort(nums.begin(), nums.end());

        int s = nums.size();

        int i, j, k;
        int n1, n2, n3;
        int sum;

        for (i = 0; i < s; ++i) {
                n1 = nums[i];

                // no way to sum up to zero, break
                if (n1 > 0) {
                        break;
                }

                // have seen this number before, skip
                if ((i > 0) && (n1 == nums[i-1])) {
                        continue;
                }

                j = i + 1;
                k = s - 1;

                while (j < k) {
                        n2 = nums[j];
                        n3 = nums[k];
                        sum = n1 + n2 + n3;
                        if (sum == 0) {
                                results.push_back({n1, n2, n3});
                                // skip if repeating
                                while ((j < k) && (nums[j] == n2)) {
                                        j++;
                                }

                                while ((j < k) && (nums[k] == n2)) {
                                        k--;
                                }
                        }
                        else if (sum < 0) {
                                j++;
                        }
                        else {
                                k--;
                        }
                }
        }

        return results;
}
};


//
int main() {
        vector<int> nums = {-1,0,1,2,-1,-4};
        Solution foo = Solution();
        vector<vector<int> >  results = foo.threeSum(nums);
        for (const auto result: results) {
                for (const auto n: result) {
                        cout << n << ' ';
                }
                cout << endl;
        }
        return 0;
}
