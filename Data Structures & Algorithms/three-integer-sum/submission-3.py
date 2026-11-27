class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i = 0
        out = []
        nums.sort()

        while i < len(nums) - 1 and nums[i] <= 0:
            if i > 0 and nums[i-1] == nums[i]:
                i += 1
                continue

            j, k = i+1, len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]

                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1

            i += 1

        return out

# Two pointers
# i goes from left to right
# In every iteration of i
    # Skip duplicates if prev same
    # j = i+1, k at right end
    # If 3sum > 0 shift k left
    # If 3sum < 0 shift j right
    # If 3sum
        # Add to out
        # Shift k left and j right
        # Keep skipping j right while prev same
