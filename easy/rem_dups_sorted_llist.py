'''

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.



Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return ListNode(head.val)
        unique_ll = ListNode(head.val)
        curr = unique_ll
        while head is not None:
            if curr.val != head.val:
                curr.next = ListNode(head.val)
                curr = curr.next
            head = head.next
        return unique_ll

result = Solution.deleteDuplicates(Solution(), )

'''
1 ListNode{val: 1, next: ListNode{val: 2, next: None}}
0
1 ListNode{val: 2, next: None}


'''

"""
TOP:


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = head
    while dummy: 
        while dummy.next and dummy.val == dummy.next.val:
            dummy.next = dummy.next.next
        dummy = dummy.next
    return head
        

"""