// Given an array, rotate the array to the right by k steps, where k is non-negative.
//
// Example 1:
//
// Input: [1,2,3,4,5,6,7] and k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]
// Example 2:
//
// Input: [-1,-100,3,99] and k = 2
// Output: [3,99,-1,-100]
// Explanation:
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]
// Note:
//
// Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
// Could you do it in-place with O(1) extra space?
//
// # %%


//
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Solution 1

class Solution {
public:
void rotate(vector<int>& nums, int k) {
        int s = nums.size();
        int count = 0;
        int start;

        for (int start = 0; count < s; start++) {
                int curPosition = start; //

                int currentValue = nums[curPosition]; // value to be put in the right position

                int nextPosition;

                do {
                        nextPosition = (curPosition + k) % s;
                        cout << curPosition << " " << nextPosition << endl;

                        int temp = nums[nextPosition];
                        nums[nextPosition] = currentValue;
                        currentValue = temp;

                        curPosition = nextPosition;
                        count++;
                        // next = (next + k) % s;

                }
                while (curPosition != start); // stop looping since start is already in right place

        }
        return;
}
};

// Solution 2
// https://www.geekxh.com/1.0.数组系列/004.html

class Solution2 {
public:
void swap(int& x, int&y){
        int temp;
        temp = x;
        x = y;
        y = temp;
        return;
}

void reverse(vector<int>& nums, int start, int end) {
        // reverse subvector from location start to end
        int count = 0; // current number of switches
        // int i = start;
        // int s = nums.size();
        int s = end - start + 1;
        int m = s / 2; // total number of switches
        // switch m mtimes to reverse
        while (count < m) {
                swap(nums[start + count], nums[end - count]);
                count++;
        }
        return;
}

void rotate(vector<int>& nums, int k) {
        // int i = 0;
        int i = 0;
        int s = nums.size();

        k = k % s;

        // reverse whole vector
        reverse(nums, 0, s - 1);

        // reverse first k elements
        reverse(nums, 0, k - 1);

        // reverse the rest
        reverse(nums, k, s - 1);


        return;
}
};

//

int main() {
        std::vector<int> nums = { 1, 2, 3,4, 5};
        int k = 2;

        // prices.push_back(10);
        // prices.push_back(20);
        // prices.push_back(30);

        Solution foo = Solution();
        foo.rotate(nums, k);
        // foo.reverse(nums, 2, 4);

        // cout<<"out put ";
        for (const auto i: nums)
                cout << i << ' ';
        // int x = 0;
        // int y = 1;
        // foo.swap(x, y);
        // cout << x << ' ';
        // cout << y << ' ';
        return 0;
}
