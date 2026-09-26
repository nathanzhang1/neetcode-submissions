class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Check rows
        for i in range(0, 9):
            seen = set()
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
            seen.clear()
        
        # Check cols
        for j in range(0, 9):
            seen = set()
            for i in range(0, 9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
            seen.clear()
        
        # Check 3x3s
        boundaries = [
        ((0, 0), (2, 2)),
        ((0, 3), (2, 5)),
        ((0, 6), (2, 8)),
        ((3, 0), (5, 2)),
        ((3, 3), (5, 5)),
        ((3, 6), (5, 8)),
        ((6, 0), (8, 2)),
        ((6, 3), (8, 5)),
        ((6, 6), (8, 8))]

        for b in boundaries:
            s_i, s_j = b[0]
            e_i, e_j = b[1]
            seen = set()
            for i in range(s_i, e_i+1):
                for j in range(s_j, e_j+1):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            seen.clear()
        
        return True


# Note: matrix[row][col]
# 3 loops?
# For each row
    # Init seen set and go through each cell
    # If we see repeat ret F
# For each col do the same
# Box ranges:
    # (0, 0) -> (2, 2), (0, 3) -> (2, 5), (0, 6) -> (2, 8)
    # (2, 0) -> (5, 2), (2, 3) -> (5, 5), (2, 6) -> (5, 8)
    # (5, 0) -> (8, 2), (5, 3) -> (8, 5), (5, 6) -> (8, 8)
