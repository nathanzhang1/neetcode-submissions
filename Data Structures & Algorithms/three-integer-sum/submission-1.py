class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i-1]:
                continue

            left, right = i+1, len(nums) - 1

            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == -nums[i]:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif cur_sum > -nums[i]:
                    right -= 1
                elif cur_sum < -nums[i]:
                    left += 1

        return output