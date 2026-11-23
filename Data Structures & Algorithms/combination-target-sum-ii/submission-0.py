class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        output = []

        candidates.sort()

        def dfs(i, cur):
            if sum(cur) > target:
                return
            
            if sum(cur) == target:
                output.append(cur)
                return
            
            if i >= n:
                return

            # Don't pick, go to next, skip any dups
            j = i+1
            while j < n and candidates[j] == candidates[i]:
                j += 1
            dfs(j, cur)

            # Pick i, go to next
            dfs(i+1, cur + [candidates[i]])
        
        dfs(0, [])

        return output

# Modification from Comb Sum 1: this time we can't stay at the same number, allowed nums pointer must always move forward