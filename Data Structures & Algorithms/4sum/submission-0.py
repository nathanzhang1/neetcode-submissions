class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        a = 0
        out = []
        n = len(nums)

        while a < n:
            if a > 0 and nums[a-1] == nums[a]:
                a += 1
                continue

            b = a+1
            while b < n:
                if b > a+1 and nums[b-1] == nums[b]:
                    b += 1
                    continue
                
                c, d = b+1, n-1
                while c < d:
                    fourSum = nums[a] + nums[b] + nums[c] + nums[d]
                    if fourSum < target:
                        c += 1
                    elif fourSum > target:
                        d -= 1
                    else:
                        out.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c-1] == nums[c]:
                            c += 1
                b += 1
            a += 1
        
        return out
                

# Two pointers: a b outer loops, c d inner
# a goes from 0 to n-1, b goes from a+1 to n-1
    # Skip dups at a and b
    # c at b+1, d at n-1
    # While c < d
        # If 4sum < 0 move c right
        # If 4sum > 0 move d left
        # If 4sum
            # Add 4sum to out
            # Move c right, d left
            # Skip dups at c