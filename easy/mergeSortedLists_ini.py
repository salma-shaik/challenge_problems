# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):

        if not list1 and not list2:
            return ListNode()
        if not list1:
            return list2
        if not list2:
            return list1

        curr1 = list1
        curr2 = list2

        i = 0

        merged_list = None

        while curr1 is not None and curr2 is not None:
            next_node = None
            if curr1.val == curr2.val:
                next_node = ListNode(curr2.val)  #
                curr = ListNode(curr1.val, next_node)  #
                curr1 = curr1.next  #
                curr2 = curr2.next  # {3, {4, None}}
            elif curr1.val < curr2.val:
                next_node = ListNode(curr2.val)  # {3, None}
                curr = ListNode(curr1.val, next_node)  # {2, {3, None}}
                curr1 = curr1.next  # {4, None}
            else:
                next_node = ListNode(curr1.val)
                curr = ListNode(curr2.val, next_node)
                curr2 = curr2.next
            if curr is not None:  # {1, {1, None}}
                if merged_list is None:
                    print('if: ', curr.val)
                    head_node = ListNode(curr.val, curr.next)  # {1, {1, None}}
                    merged_list = head_node  # {1, {1, None}}
                elif merged_list.next is None:
                    merged_list.next = ListNode(curr.val, curr.next)
                else:
                    print('else: ', curr.val)
                    merged_list.next.next = ListNode(curr.val, curr.next)  # {1, {1, None}}.       {2, {3, None}}

        while curr1 is not None:
            merged_list.next = ListNode(curr1.val, curr1.next)
            curr1 = curr1.next
        while curr2 is not None:
            merged_list.next = ListNode(curr2.val, curr2.next)
            curr2 = curr2.next

        return head_node




