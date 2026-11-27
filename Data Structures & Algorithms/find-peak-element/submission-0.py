class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            left = nums[m-1] if m-1 >= 0 else float('-inf')
            right = nums[m+1] if m+1 < len(nums) else float('-inf')

            if left < nums[m] and nums[m] > right:
                return m
            elif left < nums[m] < right:
                l = m+1
            else:
                r = m-1

# Binary search
# If m-1 < m > m+1 we found peak at m
# If m-1 < m < m+1 look right
# If m-1 > m > m+1 look left
# If m-1 > m < m+1 look either way