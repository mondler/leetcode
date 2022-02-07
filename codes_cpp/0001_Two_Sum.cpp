// 1. Two Sum
// Easy
//
// 20823
//
// 727
//
// Add to List
//
// Share
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
// You can return the answer in any order.
//
//
//
// Example 1:
//
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Output: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:
//
// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:
//
// Input: nums = [3,3], target = 6
// Output: [0,1]

#include <iostream>
#include <vector>
// #include <string>
using namespace std;
#include <unordered_map>

//
class Solution {
public:
vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        unordered_map<int, int> hash_map;

        int s = nums.size();

        for (int i=0; i < s; i++) {
                int n = nums[i];

                // if found a pair
                if (hash_map.count(target - n) == 1) {
                        res.push_back(hash_map[target - n]);
                        res.push_back(i);
                        return res;
                }

                hash_map[n] = i;
        }

        return res;
}
};

//
int main() {
        std::vector<int> nums = {3, 2, 4};
        int target = 6;

        Solution foo = Solution();
        vector<int> res = foo.twoSum(nums, target);

        for (const auto i: res)
                cout << i << ' ';

        return 0;
}
