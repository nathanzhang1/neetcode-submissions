import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0

        if len(nums1) == 0 or len(nums2) == 0:
            A = nums1 if len(nums2) == 0 else nums2
            m = len(A) // 2
            if len(A) % 2 == 0:
                return (A[m] + A[m-1]) / 2
            else:
                return A[m]

        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        
        total = len(A) + len(B)
        half = total // 2
        left, right = 0, len(A) # Use count of elements taken from each array instead of index

        while left <= right:
            # Count of elements taken from A
            m = (left + right) // 2 

            # Count of elements taken from B
            n = half - m

            A_left = A[m-1] if m > 0 else -math.inf
            A_right = A[m] if m < len(A) else math.inf
            B_left = B[n-1] if n > 0 else -math.inf
            B_right = B[n] if n < len(B) else math.inf

            if B_left > A_right:
                left = m+1
            elif A_left > B_right:
                right = m-1
            else:
                if total % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return min(A_right, B_right)
                    
        
# Binary search solution:

# We find where the merged array would be split -> median is at the boundary (dependent on odd/even length)
# Let the shorter array be A and the other B, total = len(A) + len(B), half = total // 2
# Do binary search on A to find m = number of items to take from A, then n = num taken from B = half - m
    # Start with left at start of A, right at end of A, m at middle of A
    # We have found correct position for m when A[m-1] <= B[half-m] and B[half-m-1] <= A[m]
    # If B[half-m-1] > A[m] then set left = m+1
    # If A[m-1] > B[half-m] then set right = m-1