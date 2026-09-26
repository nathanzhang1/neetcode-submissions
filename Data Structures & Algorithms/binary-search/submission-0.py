class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            midpt = (left_index + right_index) // 2
            if nums[midpt] == target:
                return midpt
            if nums[midpt] > target:
                right_index = midpt - 1
            if nums[midpt] < target:
                left_index = midpt + 1
        
        return -1

            