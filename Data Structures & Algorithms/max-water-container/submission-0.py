class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, left, right = 0, 0, len(height) - 1
        
        while left != right:
            area = (right - left) * min(height[left], height[right])
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            elif height[left] >= height[right]:
                right -= 1
        
        return max_area
        


# Move the pointer to the lower bar and keep track of max area until l = r, greedy