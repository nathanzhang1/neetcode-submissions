# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = []
        l1_ptr = list1
        l2_ptr = list2

        if list1 is None and list2 is None:
            return list1

        while l1_ptr is not None or l2_ptr is not None:
            new_node = ListNode()
            if l2_ptr is None:
                if len(sorted_list) > 0:
                    sorted_list[-1].next = new_node
                new_node.val = l1_ptr.val
                new_node.next = None
                sorted_list.append(new_node)
                l1_ptr = l1_ptr.next
            elif l1_ptr is None:
                if len(sorted_list) > 0:
                    sorted_list[-1].next = new_node
                new_node.val = l2_ptr.val
                new_node.next = None
                sorted_list.append(new_node)
                l2_ptr = l2_ptr.next
            elif l1_ptr.val <= l2_ptr.val:
                if len(sorted_list) > 0:
                    sorted_list[-1].next = new_node
                new_node.val = l1_ptr.val
                new_node.next = None
                sorted_list.append(new_node)
                l1_ptr = l1_ptr.next
            else:
                if len(sorted_list) > 0:
                    sorted_list[-1].next = new_node
                new_node.val = l2_ptr.val
                new_node.next = None
                sorted_list.append(new_node)
                l2_ptr = l2_ptr.next

        return sorted_list[0]
        