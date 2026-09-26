class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid) # Row
        n = len(grid[0]) # Col
        fresh_count = 0
        rotten_queue = deque()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    fresh_count += 1
                elif cell == 2:
                    rotten_queue.append((i, j))
        
        if not fresh_count:
            return 0
        if not rotten_queue:
            return -1
        
        minute = 0
        while True:
            new_queue = deque()
            while rotten_queue:
                row, col = rotten_queue.popleft()
                print(f"row: {row}, col: {col}")
                if row-1 >= 0 and grid[row-1][col] == 1:
                    new_queue.append((row-1, col))
                    grid[row-1][col] = 2
                    fresh_count -= 1
                if col-1 >= 0 and grid[row][col-1] == 1:
                    new_queue.append((row, col-1))
                    grid[row][col-1] = 2
                    fresh_count -= 1
                if row+1 < m and grid[row+1][col] == 1:
                    new_queue.append((row+1, col))
                    grid[row+1][col] = 2
                    fresh_count -= 1
                if col+1 < n and grid[row][col+1] == 1:
                    new_queue.append((row, col+1))
                    grid[row][col+1] = 2
                    fresh_count -= 1
            if not new_queue:
                break
            rotten_queue = new_queue.copy()
            minute += 1
        
        if fresh_count > 0:
            return -1
        
        return minute
            