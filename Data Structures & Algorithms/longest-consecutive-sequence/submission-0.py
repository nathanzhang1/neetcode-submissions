class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        seq_starts = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                seq_starts.remove(num)

        longest = 1
        for start in seq_starts:
            cur_length = 1
            cur_num = start + 1
            while cur_num in nums_set:
                cur_length += 1
                cur_num += 1
            if cur_length > longest:
                longest = cur_length
        
        return longest

# Convert list to hash set, and only keep nums in set of potential seq starters if num - 1 is not in the hash set. Then can just trivially find longest seq