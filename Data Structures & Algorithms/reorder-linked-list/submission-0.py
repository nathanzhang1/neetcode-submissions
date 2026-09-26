# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast.next:
            fast = fast.next
            if not fast.next:
                break
            fast = fast.next
            slow = slow.next
        
        cur, prev = slow.next, None
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        cur, cur2 = head, prev

        while cur2:
            temp1 = cur.next
            temp2 = cur2.next
            cur.next = cur2
            cur2.next = temp1
            cur = temp1
            cur2 = temp2