# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i, j = headA, headB

        while True:
            if i == j:
                return i
            
            if i == None:
                i = headB
                continue
            
            if j == None:
                j = headA
                continue
            
            i = i.next
            j = j.next
        
# Pointers i and j, i starts at A, j starts at B, moving one node at a time
# When they reach end, set them to the head of other list
# Eventually they will meet, return that node (or both gets to None at the same time)