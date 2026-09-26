class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out_list = []
        outer = 0
        nums.sort()
        while outer < len(nums):
            if nums[outer] > 0:
                break
            if outer > 0 and nums[outer-1] == nums[outer]:
                outer += 1
                continue
            left = outer + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -nums[outer]:
                    left += 1
                elif nums[left] + nums[right] > -nums[outer]:
                    right -= 1
                elif nums[left] + nums[right] == -nums[outer]:
                    out_list.append([nums[outer], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            outer += 1
        return out_list


# Left and right pointer

# [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]
# -nums[i] = nums[j] + nums[k]