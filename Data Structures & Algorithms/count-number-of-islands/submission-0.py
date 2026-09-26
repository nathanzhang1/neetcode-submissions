class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0" or (row, col) in visited:
                return
            
            visited.add((row, col))

            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row-1, col)

        islands = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1
        
        return islands