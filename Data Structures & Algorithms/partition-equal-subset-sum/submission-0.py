class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        sums = set()
        sums.add(0)
        sums.add(nums[len(nums) - 1])
        if target in sums:
            return True

        i = len(nums) - 2
        while i >= 0:
            new_sums = []
            for num in sums:
                new_sums.append(num + nums[i])
            
            for num in new_sums:
                sums.add(num)
            
            if target in sums:
                return True
            
            i -= 1
        
        return False

# DP intuition: at each number we either pick it or don't, aim is to get to target
# So at each number keep track of the potential sums of a subset
# Bottom-up: from back to front
    # At the start add 0, last num to set
    # For each number in set, add num_i + num to set
    # If target is in set return true

        # cache = [[0 for _ in range(total)] for _ in range(len(nums))]

        # def check(target, i):
        #     if target == 0:
        #         return True
        #     if i >= len(nums) or target < 0:
        #         return False
            
        #     if cache[i][target] == 1:
        #         return True
        #     elif cache[i][target] == 2:
        #         return False
            
        #     left = check(target - nums[i], i+1)
        #     right = check(target, i+1)

        #     cache[i][target] = 1 if left or right else 2

        #     return left or right

        # return check(target, 1) or check(target - nums[0], 1)

        
# Backtracking:
# First get sum and target = sum / 2, if sum not even return false
# Go through nums, at each num either pick num or don't
    # Check 1: check(target - curSum, i+1)
    # Check 2: check(target, i+1)
    # Return true if find target = 0