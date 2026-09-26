from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cur_LIS = []

        for num in nums:
            if not cur_LIS or cur_LIS[-1] < num:
                cur_LIS.append(num)
            else:
                i = bisect_left(cur_LIS, num)
                cur_LIS[i] = num
        
        return len(cur_LIS)