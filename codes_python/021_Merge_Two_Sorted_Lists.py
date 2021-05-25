# 21. Merge Two Sorted Lists
# Easy
#
# 6729
#
# 772
#
# Add to List
#
# Share
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
#
#
#
# Example 1:
#
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: l1 = [], l2 = []
# Output: []
# Example 3:
#
# Input: l1 = [], l2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.
# Accepted
# 1,418,826
# Submissions
# 2,504,665

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = ListNode(val=None)
        temp = head

        while ((l1 != None) and (l2 != None)):
            if l1.val <= l2.val:
                temp.next = l1
                temp = l1
                l1 = l1.next
            else:
                temp.next = l2
                temp = l2
                l2 = l2.next

        if (l2 != None):
            temp.next = l2
        if (l1 != None):
            temp.next = l1

        return head.next


# %%

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


def printlink(l: ListNode):
    temp = l
    while temp != None:
        print(temp.val)
        temp = temp.next


n1 = [1, 2, 3]
l1 = lst2link(n1)

n2 = [1, 3, 4]
l2 = lst2link(n2)

res = Solution().mergeTwoLists(l1, l2)
print('res:')
printlink(res)
print('\n')


print('l1:')
printlink(l1)
print('\n')
print('l2:')
printlink(l2)
print('\n')
