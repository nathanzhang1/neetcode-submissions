class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []
        n = len(candidates)

        def dfs(i, cur):
            if sum(cur) > target:
                return
            
            if sum(cur) == target:
                output.append(cur)
                return
            
            dfs(i, cur + [candidates[i]])
            for j in range(i+1, n):
                dfs(j, cur + [candidates[j]])
            
        dfs(0, [])
        return output

# Build up combination starting with [], at each step choose to keep adding same number or skip to any of next numbers and adding that number, once we move to next number we cant choose previous numbers, terminate branch if reaches target or surpass