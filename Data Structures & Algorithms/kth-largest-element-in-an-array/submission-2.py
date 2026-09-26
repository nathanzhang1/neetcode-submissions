import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [-x for x in nums]
        heapq.heapify(neg_nums)

        for i in range(k-1):
            heapq.heappop(neg_nums)
        
        return -1 * heapq.heappop(neg_nums)
        



        # QUICK SELECT SOLUTION:
        
        # diff = len(nums) - k
        
        # def quickSelect(l, r):
        #     pivot = nums[r]
        #     p = l

        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[i], nums[p] = nums[p], nums[i]
        #             p += 1
            
        #     nums[r], nums[p] = nums[p], nums[r]

        #     if diff > p:
        #         return quickSelect(p+1, r)
        #     elif diff < p:
        #         return quickSelect(l, p-1)
        #     else:
        #         return nums[p]

        # return quickSelect(0, len(nums) - 1)