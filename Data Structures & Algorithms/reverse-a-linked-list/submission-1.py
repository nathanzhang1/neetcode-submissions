# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, cur = None, head

        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp
        
        return prev
        
# Prev starts as None, cur starts as first node
# While prev has not reached the end
    # Set temp = cur
    # Move cur to cur.next
    # Set temp.next to prev
    # Set prev to temp