// Given an array nums and a value val, remove all instances of that value in-place and return the new length.
//
// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
//
// The order of elements can be changed. It doesn't matter what you leave beyond the new length.
//
// Example 1:
//
// Given nums = [3,2,2,3], val = 3,
//
// Your function should return length = 2, with the first two elements of nums being 2.
//
// It doesn't matter what you leave beyond the returned length.
// Example 2:
//
// Given nums = [0,1,2,2,3,0,4,2], val = 2,
//
// Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
//
// Note that the order of those five elements can be arbitrary.
//
// It doesn't matter what values are set beyond the returned length.

#include <iostream>
#include <vector>
#include <string>
using namespace std;

//

class Solution {
public:

void swap(int& x, int&y){
        int temp;
        temp = x;
        x = y;
        y = temp;
        return;
}

int removeElement(vector<int>& nums, int val) {
        int i, j;
        i = 0;
        j = 0;
        int s = nums.size();

        while ((i < s) && (j < s)) {
                while ((i < s) && (nums[i] != val)) {
                        i++;
                }
                j = max(j, i + 1);
                while ((j < s) && (nums[j] == val)) {
                        j++;
                }
                // cout << i << ' ' << j << endl;
                if ((i < s) && (j < s)) {
                        swap(nums[i], nums[j]);
                }
        }

        return i;
}
};

//

int main() {
        std::vector<int> nums = {1,2,2,3};
        int val = 2;

        Solution foo = Solution();
        cout << foo.removeElement(nums, val) << endl;

        for (const auto i: nums)
                cout << i << ' ';

        return 0;
}
