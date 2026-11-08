class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        out = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(row, col):
            stack = [(row, col)]
            visited.add((row, col))
            is_closed = True
            
            while stack:
                r, c = stack.pop()
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                    is_closed = False
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
            
            return is_closed

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if dfs(i, j):
                        out += 1
        
        return out

        
# Island is not closed if it touches the border
# Go through the grid
    # If we see land that has not been visited
        # Do recursive DFS, marking each cell visited as we go
        # If we touch a border, mark this island is not closed
        # If DFS returns without any cell touching border, add to count