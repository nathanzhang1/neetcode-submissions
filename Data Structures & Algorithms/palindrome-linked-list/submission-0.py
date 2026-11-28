# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, cur = None, slow
        
        while cur:
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True


# Slow and fast pointers and stop when fast at end/surpass end, slow at middle
# Reverse linked list starting at slow until end
# Traverse down list from both ends, comparing each node until right end hits none