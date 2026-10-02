class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0

        for cur_i, cur_h in enumerate(heights):
            start_i = cur_i
            while stack and stack[-1][1] > cur_h:
                top_i, top_h = stack.pop()
                maxArea = max(maxArea, top_h * (cur_i - top_i))
                start_i = top_i
            stack.append((start_i, cur_h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea


# Keep monotonic stack of (start_index, height) of increasing height
# For each height at index i:
    # While stack isnt empty and top height > cur_height:
        # Pop and retrieve top of stack: top[h] and top[i]
        # Max area at this point = top[h] * (i - top[i]), update global maxArea if possible
        # Update start_i = top[i]
    # Push (start_i, cur_height) onto stack
# For each remaining (i, h) in stack:
    # Max area at this height = h * (number of bars - i), update global maxArea if possible