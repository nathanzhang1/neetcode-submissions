from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        left, right = 0, k-1
        out = []

        for i in range(0, k):
            while dq and nums[i] > dq[-1]:
                dq.pop()
            dq.append(nums[i])
        
        out.append(dq[0])
        left += 1
        right += 1
        if len(nums) > 1 and nums[left-1] == dq[0]:
            dq.popleft()

        while right < len(nums):
            while dq and nums[right] > dq[-1]:
                dq.pop()
            dq.append(nums[right])
            out.append(dq[0])
            left += 1
            right += 1
            if nums[left-1] == dq[0]:
                dq.popleft()
        
        return out



# Monotonic queue solution:

# Init left = 0, right = k-1, deque
# First process initial window state:
    # For each num:
        # While cur num > left of queue popleft (until queue empty or cur num <= left of queue)
        # Append cur num to queue
    # Add left of queue to out list
    # Advance left and right
# While right is not at end:
    # If left of window = left of queue (we are about to skip over the current highest num)
        # Popleft once
    # While right of window > left of queue popleft
    # Append cur num to queue
    # Add left of queue to out list
    # Advance left and right