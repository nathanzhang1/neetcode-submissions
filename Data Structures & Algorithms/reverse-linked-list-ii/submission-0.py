# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(-1, head)
        prev, cur = dummy, head
        
        for _ in range(left-1):
            cur = cur.next
            prev = prev.next
        
        first = prev
        prev = None

        for _ in range(right-left+1):
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp
        
        temp = first.next
        first.next = prev
        temp.next = cur

        return dummy.next
        
    
# Dummy node points to head
# Set prev = dummy, cur = head and go down list until cur has travelled left-1 nodes
# Set first = prev
# Set prev = None
# Move cur down right - left + 1 times
    # temp = cur
    # cur = cur.next
    # temp.next = prev
    # prev = temp
# temp = first.next
# first.next = prev
# temp.next = cur