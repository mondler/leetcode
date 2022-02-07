# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Share
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Follow up: Could you do this in one pass?
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # first go n steps from head
        rightNode = head
        for i in range(n):
            rightNode = rightNode.next

        # if need to delete the first
        if (rightNode == None):
            return head.next

        leftNode = head

        # leftNode will point to (n+1) from end
        while (rightNode.next != None):
            leftNode = leftNode.next
            rightNode = rightNode.next

        leftNode.next = leftNode.next.next
        return head

# %%


n5 = ListNode(val=5)
n4 = ListNode(val=4, next=n5)
n3 = ListNode(val=3, next=n4)
n2 = ListNode(val=2, next=n3)
n1 = ListNode(val=1, next=n2)

# n = n1
# while n != None:
#     print(n.val)
#     n = n.next

head = Solution().removeNthFromEnd(n4, 1)

# head

n = head
while n != None:
    print(n.val)
    n = n.next
