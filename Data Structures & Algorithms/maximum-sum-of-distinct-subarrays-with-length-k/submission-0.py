class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        left, right = 0, k-1
        curSum = 0
        counts = {}
        repeats = set()

        for i in range(k):
            cur = nums[i]
            if cur not in counts:
                counts[cur] = 0

            counts[cur] += 1

            if counts[cur] == 2:
                repeats.add(cur)
            
            curSum += cur

        curMaxSum = curSum if len(repeats) == 0 else 0
        
        left += 1
        right += 1

        while right < len(nums):
            counts[nums[left-1]] -= 1
            if counts[nums[left-1]] == 1:
                repeats.remove(nums[left-1])
            
            if nums[right] not in counts:
                counts[nums[right]] = 0
            counts[nums[right]] += 1
            if counts[nums[right]] == 2:
                repeats.add(nums[right])
            
            curSum = curSum - nums[left-1] + nums[right]

            if len(repeats) == 0:
                curMaxSum = max(curMaxSum, curSum)
            
            left += 1
            right += 1
        
        return curMaxSum

# Sliding window:
# Set left = 0, right = k-1, curMaxSum = 0, curSum = 0
# Process first window:
    # Add each element to hash table: element -> count
    # If any element >1 count, add to hash set
    # Update curSum
    # Only update curMaxSum for first window if hash set empty
    # Move left and right pointers
# While right not at end of array
    # Decrement map[nums[left-1]], if decrement to 1 remove left-1 from hash set
    # Increment map[nums[right]], if increment to 2 add right to hash set
    # Update curSum = curSum - nums[left-1] + nums[right]
    # Update curMaxSum if hash set empty