// 102. Binary Tree Level Order Traversal
// Medium
//
// 5042
//
// 109
//
// Add to List
//
// Share
// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
//
//
//
// Example 1:
//
//
// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[9,20],[15,7]]
// Example 2:
//
// Input: root = [1]
// Output: [[1]]
// Example 3:
//
// Input: root = []
// Output: []
//
//
// Constraints:
//
// The number of nodes in the tree is in the range [0, 2000].
// -1000 <= Node.val <= 1000
// Accepted
// 882,579
// Submissions
// 1,524,773

#include <iostream>
// #include <algorithm>    // std::sort
// #include <vector>       // std::vector
// #include <string>
// #include <unordered_map>
#include <queue>

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


void printVecVec(vector<vector<int> > vv) {
        for (vector<int> row: vv)
        {
                for (int val: row) {
                        cout << val << " ";
                }
                cout << endl;
        }
        cout << endl;
};

class Solution {
public:
vector<vector<int> > levelOrder(TreeNode* root) {
        vector<vector<int> > res;
        // res = levelOrderBFS(root);
        levelOrderDFS(root, 0 /* depth */, res);
        return res;
}
private:
vector<vector<int> > levelOrderBFS(TreeNode* root) {
        vector<vector<int> > res;

        if (!root) {
                return res;
        }

        queue<TreeNode*> curr; // current layer to loop over
        curr.push(root);

        while (!curr.empty()) {
                res.push_back({}); // vector for a new layer
                queue<TreeNode*> next; // to save nodes for next run

                while (!curr.empty()) { // loop over the current layer
                        TreeNode* tnp = curr.front();
                        curr.pop();
                        res.back().push_back(tnp->val);
                        if (tnp->left) {
                                next.push(tnp->left);
                        }
                        if (tnp->right) {
                                next.push(tnp->right);
                        }
                }

                curr.swap(next);
        }
        return res;
}
void levelOrderDFS(TreeNode* root, int depth, vector<vector<int> >& ans) {
        if(!root) return;
        // Works with pre/in/post order
        while(ans.size() <= depth) {
                ans.push_back({});
        };
        ans[depth].push_back(root->val); // pre-order
        levelOrderDFS(root->left, depth+1, ans);
        levelOrderDFS(root->right, depth+1, ans);
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

        // queue<int> level;
        //
        // level.push(1);
        // level.push(2);
        // level.push(3);
        //
        // cout << level.front() << endl;


        auto foo = Solution();
        auto res = foo.levelOrder(t0);
        printVecVec(res);



        return 0;
}
