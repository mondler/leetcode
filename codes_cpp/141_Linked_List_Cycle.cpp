// https://leetcode.com/problems/linked-list-cycle/
// 141. Linked List Cycle
// Easy
//
// 2249
//
// 339
//
// Add to List
//
// Share
// Given a linked list, determine if it has a cycle in it.
//
// To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
//
// https://leetcode.com/problems/linked-list-cycle/description/
//
// %%
//
// Definition for singly-linked list.
// class ListNode(object):
//     def __init__(self, x):
//         self.val = x
//         self.next = None
//
// slow and fast runner will finally meet if cycle exists
// https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare

#include <iostream>
// #include <algorithm>    // std::sort
// #include <vector>       // std::vector
// #include <string>
#include <unordered_map>

using namespace std;





struct ListNode {
        int val;
        ListNode *next;
        // ListNode(int x) : val(x), next(NULL) {
        // }
};


class Solution {
public:

bool hasCycle(ListNode *head) {
        if (head==NULL) {
                return false;
        }

        // fast will move two steps a time
        ListNode* fast = head;
        // head is being slow (moving one step at a time)

        // ListNode* slow = head;

        // while ((fast->next != NULL) && ((fast->next)->next != NULL)) {
        while (fast && fast->next) {
                /* code */
                fast = (fast->next)->next;
                // cout << "fast at " << fast->val << endl;
                head = head->next;
                // cout << "slow at " << slow->val << endl;
                if (fast == head) {
                        return true;
                }
        }

        return false;

}

bool hasCycle2(ListNode *head) {

        if (head==NULL) {
                return false;
        }

        unordered_map<ListNode*, int> umap;

        // ListNode* temp = head;

        while (head->next != NULL) {
                // Key is not present
                if (umap.find(head) == umap.end()) {
                        // cout << head->val << " not added to Map yet" << endl;
                        umap[head] = 1;
                        head = head->next;
                }
                else {
                        // cout << head->val << " was in the Map" << endl;
                        return true;
                }
                // return "Not Present";
        }

        return false;
}
};

int main() {
        ListNode* head = NULL;
        ListNode* second = NULL;
        ListNode* third = NULL;

        head = new ListNode();
        second = new ListNode();
        third = new ListNode();

        head->val = 1;
        head->next = second;

        second->val = 2;
        second->next = third;

        third->val = 3;
        third->next = NULL;


        Solution foo = Solution();
        bool res = foo.hasCycle(head);
        cout << res << endl;
        return 0;
}
