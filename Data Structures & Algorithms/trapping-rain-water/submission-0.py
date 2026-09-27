class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[0], height[len(height) - 1]
        out = 0

        while left < right:
            if maxLeft <= maxRight:
                out += max(0, maxLeft - height[left])
                left += 1
                maxLeft = max(maxLeft, height[left])
            elif maxRight < maxLeft:
                out += max(0, maxRight - height[right])
                right -= 1
                maxRight = max(maxRight, height[right])
        
        return out
        
# Overarching algorithm: water trapped at i = min(maxLeft, maxRight) - height[i] where maxLeft and maxRight is the maximum height of blocks to the left and right of block i

# Two pointers approach:

# Init with left at start, right at end moving towards each other
# While left < right
    # If maxLeft <= maxRight:
        # Water trapped at left = maxLeft - height[left]
        # Move left
        # Update maxLeft if nec
    # If maxRight < maxLeft:
        # Water trapped at right = maxRight - height[right]
        # Move right
        # Update maxRight if nec
# NB: We move the pointer with the lower maxLeft or maxRight since we only care about the lower of maxLeft or maxRight, so when calculating we can disregard the max of the other side