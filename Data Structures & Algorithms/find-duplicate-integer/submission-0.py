class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                break
                
        i = 0
        
        while True:
            i = nums[i]
            slow = nums[slow]

            if i == slow:
                return slow


# Think of array as an array of pointers to next index
# ie. 0 -> 3 --> 2 --> 4
#                  <--
# Now we have linked list cycle detection, find start of cycle, return val at that index