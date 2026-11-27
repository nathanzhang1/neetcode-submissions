class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) <= len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1
        
        l, r = 0, len(A) - 1
        while True:
            m = l + (r - l) // 2
            n = half - m - 2

            Al = A[m] if m >= 0 else float('-inf')
            Ar = A[m+1] if m+1 < len(A) else float('inf')
            Bl = B[n] if n >= 0 else float('-inf')
            Br = B[n+1] if n+1 < len(B) else float('inf')

            if Al <= Br and Bl <= Ar:
                if total % 2 == 1:
                    return min(Ar, Br)
                return (max(Al, Bl) + min(Ar, Br)) / 2
            elif Al > Br:
                r = m-1
            else:
                l = m+1

# Binary search
# A: 2 5 6 7 8 
# B: 1 3 4 9 10 11
# Merged 1 2 3 4 5 6 7 8 9 10 11
# Find m = end of elements of A that contribute to left half of merged array
# Also keep track of n = end of elements of B that contribute to left half of merged array, n = half - m - 2 where half = merged_length // 2
# Do binary search on A:
    # If m <= n+1 and n <= m+1, we found m
        # If odd, median = min(A_right, B_right)
        # If even, median = (max(A_left, B_left) + min(A_right, B_right)) / 2
    # If m > n+1, m is to left
    # Else m is to right