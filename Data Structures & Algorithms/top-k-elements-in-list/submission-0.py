class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_to_freq = {}
        for num in nums:
            if num not in nums_to_freq:
                nums_to_freq[num] = 1
            else:
                nums_to_freq[num] += 1
        
        print(nums_to_freq)

        tuple_list = nums_to_freq.items()
        sorted_tuple_list = list(reversed(sorted(tuple_list, key=lambda x: x[1])))

        out_list = []
        for i in range(k):
            out_list.append(sorted_tuple_list[i][0])
        
        return out_list

# Use hash map to store number to freq, then convert map to tuple and then sort the tuple based on the 
# second item using a lambda function, then add the last k first tuple values to out list