// 98. Validate Binary Search Tree
// Medium
//
// 6388
//
// 707
//
// Add to List
//
// Share
// Given the root of a binary tree, determine if it is a valid binary search tree (BST).
//
// A valid BST is defined as follows:
//
// The left subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.
//
//
// Example 1:
//
//
// Input: root = [2,1,3]
// Output: true
// Example 2:
//
//
// Input: root = [5,1,4,null,null,3,6]
// Output: false
// Explanation: The root node's value is 5 but its right child's value is 4.
//
//
// Constraints:
//
// The number of nodes in the tree is in the range [1, 104].
// -231 <= Node.val <= 231 - 1
// Accepted
// 1,018,064
// Submissions
// 3,487,382

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


class Solution { // recursion
public:
bool isValidBST(TreeNode* root) {
        return isValidBSTRecur(root, nullptr, nullptr);
}
private:
bool isValidBSTRecur(TreeNode* root, int* min_val, int* max_val){
        if (!root)
                return true;

        if (max_val && root->val >= *max_val)
                return false;
        if (min_val && root->val <= *min_val)
                return false;

        return isValidBSTRecur(root->left, min_val, &(root->val)) &&
               isValidBSTRecur(root->right, &(root->val), max_val);
};
};



class Solution2 { // in-order traversal
public:
void inOrder(TreeNode* root) {
        if (!root)
                return;
        inOrder(root->left);
        tree.push_back(root->val);
        inOrder(root->right);
}

bool isValidBST(TreeNode* root) {
        if (!root)
                return true;

        inOrder(root);
        for (int i=1; i<tree.size(); i++)
                if (tree[i] <= tree[i-1])
                        return false;
        return true;
}
private:
vector<int> tree;
};



class Solution3 { // in-order traversal, check in real time
public:
bool isValidBST(TreeNode* root) {
        // prev_ = nullptr;
        return inOrder(root);
}
private:
TreeNode* prev_;
bool inOrder(TreeNode* root) {
        if (!root) return true;
        if (!inOrder(root->left)) return false;
        // real time check
        if (prev_ && root->val <= prev_->val) return false;
        prev_ = root;
        if (!inOrder(root->right)) return false;
        return true;
}
};

int main() {

        return 0;
}
