// 104. Maximum Depth of Binary Tree
// Easy
//
// 4146
//
// 99
//
// Add to List
//
// Share
// Given the root of a binary tree, return its maximum depth.
//
// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
//
//
//
// Example 1:
//
//
// Input: root = [3,9,20,null,null,15,7]
// Output: 3
// Example 2:
//
// Input: root = [1,null,2]
// Output: 2
// Example 3:
//
// Input: root = []
// Output: 0
// Example 4:
//
// Input: root = [0]
// Output: 1
//
//
// Constraints:
//
// The number of nodes in the tree is in the range [0, 104].
// -100 <= Node.val <= 100
// Accepted
// 1,172,209
// Submissions
// 1,701,027

#include <iostream>
// #include <algorithm>    // std::sort
// #include <vector>       // std::vector
// #include <string>
// #include <unordered_map>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode() : val(0), left(nullptr), right(nullptr) {
        }
        TreeNode(int x) : val(x), left(nullptr), right(nullptr) {
        }
        TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {
        }
};

class Solution {
public:
int maxDepth(TreeNode* root) {
        if (root) {
                return (1 + max(maxDepth(root->left), maxDepth(root->right)));
        }
        else
                return 0;
}
};

int main() {
        TreeNode * t0 = new TreeNode(0);
        TreeNode * t1 = new TreeNode(1);
        TreeNode * t2 = new TreeNode(2);
        TreeNode * t3 = new TreeNode(3);
        // cout << t2->val;
        t0->left = t1;
        t0->right = t2;
        t1->left = t3;

        auto foo = Solution();

        cout << foo.maxDepth(t0) << endl;
        cout << foo.maxDepth(t3) << endl;

        // Tree
        return 0;
}
