class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        out = [[]]

        def backtrack(cur, idx):
            if idx >= len(nums):
                return
            
            for i in range(idx, len(nums)):
                new = cur.copy()
                new.append(nums[i])
                out.append(new)

                backtrack(new, i+1)

        backtrack([], 0)
        return out


# Backtracking: 
# Start with empty array, i at 0
# For each num starting at num[i], recursively backtrack and set new i so that next backtrack can only start at num[i]