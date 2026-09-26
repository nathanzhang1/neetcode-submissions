class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = set()
        risingDiagonals = set()
        fallingDiagonals = set()

        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        def dfs(col):
            if col == n:
                valid_board = ["".join(row) for row in board]
                result.append(valid_board)
                return

            for row in range(n):
                if row in rows or row+col in risingDiagonals or row-col in fallingDiagonals:
                    continue
                
                board[row][col] = 'Q'
                rows.add(row)
                risingDiagonals.add(row+col)
                fallingDiagonals.add(row-col)

                dfs(col + 1)

                board[row][col] = '.'
                rows.remove(row)
                risingDiagonals.remove(row+col)
                fallingDiagonals.remove(row-col)
        
        dfs(0)
        return result