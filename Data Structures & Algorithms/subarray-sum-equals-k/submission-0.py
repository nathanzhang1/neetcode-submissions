class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur, out = 0, 0
        prefix_sums = {}
        prefix_sums[0] = 1 # Trivial case: when we have a subarray that adds up to k we have a prefix sum of 0

        cumulative_sum = 0
        while cur < len(nums):
            cumulative_sum += nums[cur]
            target_sum = cumulative_sum - k

            if target_sum in prefix_sums:
                out += prefix_sums[target_sum]
            
            if cumulative_sum not in prefix_sums:
                prefix_sums[cumulative_sum] = 0
            prefix_sums[cumulative_sum] += 1
            
            cur += 1
        
        return out