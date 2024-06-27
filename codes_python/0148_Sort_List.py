# Given the head of a linked list, return the list after sorting it in ascending order.

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sorts a linked list in ascending order using merge sort.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The head of the sorted linked list.
        """
        # Base case: If the list is empty or has only one element,
        # it is already sorted.
        if not head or not head.next:
            return head

        # Split the list into two halves.
        left = head
        right = self.getMid(head)

        # Cut the right linked list off.
        tmp = right.next
        right.next = None
        right = tmp

        # Recursively sort the left and right halves.
        left = self.sortList(left)
        right = self.sortList(right)

        # Merge the sorted halves.
        return self.merge(left, right)

    def merge(
        self,
        head1: Optional[ListNode],
        head2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists.

        Args:
            head1 (Optional[ListNode]): The head of the first linked list.
            head2 (Optional[ListNode]): The head of the second linked list.

        Returns:
            Optional[ListNode]: The head of the merged linked list.
        """
        # Create a new head and tail node for the merged list.
        newHead = tail = ListNode()

        # Iterate through the linked lists until one of them becomes empty.
        while head1 and head2:
            # If the value in the first list is greater, add the node from the
            # second list to the merged list. Otherwise, add the node from the
            # first list.
            if head1.val > head2.val:
                tail.next = head2
                head2 = head2.next
            else:
                tail.next = head1
                head1 = head1.next
            # Move the tail pointer to the end of the merged list.
            tail = tail.next

        # Add the remaining nodes from the non-empty linked list to the merged list.
        tail.next = head1 if head1 else head2

        # Return the head of the merged list.
        return newHead.next

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Get the middle node of a linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.

        Returns:
            Optional[ListNode]: The middle node of the linked list.
        """
        # Initialize two pointers, slow and fast, to traverse the linked list.
        slow = head
        fast = head.next

        # Traverse the linked list until fast reaches the end or the next-to-last node.
        while fast and fast.next:
            # Move the slow pointer one node ahead.
            slow = slow.next
            # Move the fast pointer two nodes ahead.
            fast = fast.next.next

        # Return the slow pointer, which is now at the middle node of the linked list.
        return slow
