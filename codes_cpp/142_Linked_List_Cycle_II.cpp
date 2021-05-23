// 142. Linked List Cycle II
// Medium
//
// 4209
//
// 313
//
// Add to List
//
// Share
// Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
//
// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
//
// Notice that you should not modify the linked list.
//
//
//
// Example 1:
//
//
// Input: head = [3,2,0,-4], pos = 1
// Output: tail connects to node index 1
// Explanation: There is a cycle in the linked list, where tail connects to the second node.
// Example 2:
//
//
// Input: head = [1,2], pos = 0
// Output: tail connects to node index 0
// Explanation: There is a cycle in the linked list, where tail connects to the first node.
// Example 3:
//
//
// Input: head = [1], pos = -1
// Output: no cycle
// Explanation: There is no cycle in the linked list.
//
//
// Constraints:
//
// The number of the nodes in the list is in the range [0, 104].
// -105 <= Node.val <= 105
// pos is -1 or a valid index in the linked-list.
//
//
// Follow up: Can you solve it using O(1) (i.e. constant) memory?

#include <iostream>
// #include <algorithm>    // std::sort
// #include <vector>       // std::vector
// #include <string>
// #include <unordered_map>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
        int val;
        ListNode *next;
        // ListNode(int x) : val(x), next(NULL) {
        // }
};


class Solution {
public:
ListNode *detectCycle(ListNode *head) {
        if (head==NULL) {
                return NULL;
        }

        // fast will move two steps a time
        ListNode* fast = head;

        ListNode* slow = head;

        // while ((fast->next != NULL) && ((fast->next)->next != NULL)) {
        while (fast && fast->next) {
                /* code */
                fast = (fast->next)->next;
                // cout << "fast at " << fast->val << endl;
                slow = slow->next;
                // cout << "slow at " << slow->val << endl;
                if (fast == slow) {
                        return true;
                }
        }

        return NULL;
}
};


int main() {
        ListNode* head = NULL;
        ListNode* second = NULL;
        ListNode* third = NULL;
        ListNode* fourth = NULL;

        head = new ListNode();
        second = new ListNode();
        third = new ListNode();
        fourth = new ListNode();

        head->val = 1;
        head->next = second;

        second->val = 2;
        second->next = third;

        third->val = 3;
        third->next = fourth;

        fourth->val = 4;
        fourth->next = second;


        Solution foo = Solution();
        ListNode res = foo.detectCycle(head);
        cout << res->val << endl;
        return 0;
}
