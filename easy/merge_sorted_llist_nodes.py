from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        print(self.val, '{', self.next, ' }')

class TestHello:
    def printHello(var):
        var1 = var*10
        msg = 'hello'
        return str(var1) + msg

class NodeFromList:
    def createLLNodes(num_list):
        print(num_list)
        list_node = ListNode()
        curr = list_node

        for num in num_list:
            curr.next = ListNode(num)
            curr = curr.next

        # while list_node is not None:
        #     print(list_node.val)
        #     list_node = list_node.next

        return list_node.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        if list1 is None and list2 is None:
            return None
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None:
            return list2

        head = ListNode()
        curr = head

        while list1 is not None and list2 is not None:
            if list1.val == list2.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                curr.next = ListNode(list2.val)
                curr = curr.next

                list1 = list1.next
                list2 = list2.next

            elif list1.val < list2.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next

            else:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next

        while list1 is not None:
            curr.next = ListNode(list1.val)
            curr = curr.next
            list1 = list1.next

        while list2 is not None:
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next

        return head.next


node2 = NodeFromList.createLLNodes([1, 3, 4])

node1 = NodeFromList.createLLNodes([1, 2, 4])

res = Solution.mergeTwoLists(Solution(), node1, node2)
while res is not None:
    print(res.val)
    res = res.next


"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
    
        if list1:
            node.next = list1
        if list2:
            node.next = list2

        return head.next
"""