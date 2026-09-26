class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}

        for n in nums:
            if n not in num_to_freq:
                num_to_freq[n] = 0
            num_to_freq[n] += 1
        
        count_to_nums = [[] for _ in range(len(nums) + 1)]

        for n in num_to_freq:
            freq = num_to_freq[n]
            count_to_nums[freq].append(n)
        
        top_k = []

        for i in range(len(count_to_nums) - 1, -1, -1):
            freq = count_to_nums[i]
            if not freq:
                continue
            for num in freq:
                top_k.append(num)
                k -= 1
                if k == 0:
                    return top_k