# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        one, two = l1, l2
        carry = False
        out = None
        out_pt = None

        while one or two:
            a = one.val if one else 0
            b = two.val if two else 0

            result = a + b
            if carry:
                result += 1

            if result >= 10:
                result = result % 10
                carry = True
            else:
                carry = False
            
            if not out:
                out = ListNode(val=result)
                out_pt = out
            else:
                out_pt.next = ListNode(val=result)
                out_pt = out_pt.next
                
            one = one.next if one else None
            two = two.next if two else None
        
        if carry:
            out_pt.next = ListNode(val=1)
        
        return out


# Process each list from front to back, building the out list from front to back too
# This is possible as at num i we can add the 2 numbers together and add a node in out list, if we need to
# carry then remember that

# While not at end of both lists
    # Get both numbers a and b, or just one if the other ended already
    # Calculate result = a + b (and + 1 if carry is true)
    # If result < 10 then just add result as next node in out node
    # If result >= 10 then add the unit digit as next node in out node and flip a carry boolean to true
# If at the end carry is true add an extra 1 at the end of out list
        