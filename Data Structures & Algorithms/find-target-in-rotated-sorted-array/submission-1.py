class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        p = l

        if target <= nums[-1] and target >= nums[p]:
            l, r = p, len(nums) - 1
        else:
            l, r = 0, p - 1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        
        return -1

# Binary search to find pivot = smallest element
# If t > l
    # Binary search from 0 to p
# Else t < r
    # Binary search from p+1 to n-1