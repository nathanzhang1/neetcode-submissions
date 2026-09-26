# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        
        heap = []
        
        for i, list_head in enumerate(lists):
            if list_head:
                heapq.heappush(heap, (list_head.val, i))
        
        if not heap:
            return

        out = 0
        p = out

        while heap:
            cur_val, list_index = heapq.heappop(heap)
            lists[list_index] = lists[list_index].next
            if lists[list_index]:
                heapq.heappush(heap, (lists[list_index].val, list_index))

            if not p:
                out = ListNode()
                p = out
                p.val = cur_val
            else:
                p.next = ListNode()
                p.next.val = cur_val
                p = p.next
        
        return out