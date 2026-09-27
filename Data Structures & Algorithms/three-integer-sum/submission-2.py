class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        out_list = []

        i = 0
        
        while i < len(nums):
            if nums[i] > 0:
                break

            if i > 0 and nums[i-1] == nums[i]:
                i += 1
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                elif threeSum == 0:
                    out_list.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    
            i += 1
        
        return out_list


# Sort the list
# Outer iterator i at start moving right, skipping any duplicates
    # Left at i+1, right at end
    # While left < right
        # If i + left + right < 0, increment left
        # If i + left + right > 0, decrement right
        # If i + left + right == 0
            # Add [i, left, right] to out list
            # Increment left, skipping any duplicates
            # Decrement right
    # Increment i, skipping any duplicates

# Sample: [-4, -3, -2, -2, -1, 0, 0, 1, 2, 2, 3, 5, 6, 7]