

class ListNodeCreator:
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