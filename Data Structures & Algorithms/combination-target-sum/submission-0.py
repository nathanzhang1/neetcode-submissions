class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        out_list = []
        N = len(candidates)

        def search(arr, cur, cur_sum):
            if cur >= N:
                return
            elif cur_sum == target:
                out_list.append(arr)
                return
            elif cur_sum > target:
                return
            
            search(arr + [candidates[cur]], cur, cur_sum + candidates[cur])
            search(arr, cur + 1, cur_sum)

        search([candidates[0]], 0, candidates[0])
        search([], 1, 0)

        return out_list


# Using recursive backtracking, i to keep track of which to exclude
# Base case: cur output > target just return, cur output = target add to out list
# Left search = add num at i as fixed entry in potential output
# Right search = shift i+1, can no longer pick more nums to left of i
    # Unless shifting i+1 would put i over edge of array, stop