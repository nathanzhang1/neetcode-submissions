class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        queue = deque([(0, 0, 1)])

        visited = set()
        visited.add((0, 0))

        while queue:
            row, col, length = queue.popleft()
            print(f"row: {row}, col: {col}, len: {length}")
            if row == n-1 and col == n-1:
                return length
            
            if row+1 < n and grid[row+1][col] == 0 and (row+1, col) not in visited:
                queue.append((row+1, col, length+1))
                visited.add((row+1, col))
            if col+1 < n and grid[row][col+1] == 0 and (row, col+1) not in visited:
                queue.append((row, col+1, length+1))
                visited.add((row, col+1))
            if row-1 >= 0 and grid[row-1][col] == 0 and (row-1, col) not in visited:
                queue.append((row-1, col, length+1))
                visited.add((row-1, col))
            if col-1 >= 0 and grid[row][col-1] == 0 and (row, col-1) not in visited:
                queue.append((row, col-1, length+1))
                visited.add((row, col-1))
            if row+1 < n and col+1 < n and grid[row+1][col+1] == 0 and (row+1, col+1) not in visited:
                queue.append((row+1, col+1, length+1))
                visited.add((row+1, col+1))
            if row+1 < n and col-1 >= 0 and grid[row+1][col-1] == 0 and (row+1, col-1) not in visited:
                queue.append((row+1, col-1, length+1))
                visited.add((row+1, col-1))
            if row-1 >= 0 and col+1 < n and grid[row-1][col+1] == 0 and (row-1, col+1) not in visited:
                queue.append((row-1, col+1, length+1))
                visited.add((row-1, col+1))
            if row-1 >= 0 and col-1 >= 0 and grid[row-1][col-1] == 0 and (row-1, col-1) not in visited:
                queue.append((row-1, col-1, length+1))
                visited.add((row-1, col-1))
        
        return -1