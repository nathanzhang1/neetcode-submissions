class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0
        seen = set()

        def bfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0 or (i, j) in seen:
                return 0
            
            seen.add((i, j))

            up = bfs(i-1, j)
            down = bfs(i+1, j)
            left = bfs(i, j-1)
            right = bfs(i, j+1)

            return 1 + up + down + left + right

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in seen:
                    area = bfs(i, j)
                    max_area = max(area, max_area)
        
        return max_area


# Iterate through cells
    # If current cell is land
        # Do BFS through island
            # Start at area = 1
            # Explore 4 directions, if a direction has land and is not explored yet do BFS again + 1 with area