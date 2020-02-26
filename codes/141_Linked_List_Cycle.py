# 41. Linked List Cycle
# Easy
#
# 2249
#
# 339
#
# Add to List
#
# Share
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
# https://leetcode.com/problems/linked-list-cycle/description/

# %%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# slow and fast runner will finally meet if cycle exists
# https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

# %%
