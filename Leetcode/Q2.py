from typing import Optional

"""
You are given two non-empty linked lists representing two non-negative integers. 

The digits are stored in reverse order, and each of their nodes contains a single digit. 

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        current = res
        while (l1 and l2):
            current.val += l1.val + l2.val
            if current.val >= 10:
                current.val -= 10
                current.next = ListNode()
                current.next.val += 1
            if (l1.next or l2.next) and not current.next:
                current.next = ListNode()
            current = current.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            current.val += l1.val
            if current.val >= 10:
                current.val -= 10
                current.next = ListNode()
                current.next.val += 1
            if l1.next and not current.next:
                current.next = ListNode()
            current = current.next
            l1 = l1.next
        while l2:
            current.val += l2.val
            if current.val >= 10:
                current.val -= 10
                current.next = ListNode()
                current.next.val += 1
            if l2.next and not current.next:
                current.next = ListNode()
            current = current.next
            l2 = l2.next
        return res
