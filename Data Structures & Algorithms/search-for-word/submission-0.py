class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) # Row
        n = len(board[0]) # Col

        visited = set()
        def bfs(row, col, word_idx):
            visited.add((row, col))

            if word_idx == len(word) - 1:
                return True
            
            if row-1 >= 0 and board[row-1][col] == word[word_idx+1] and (row-1, col) not in visited:
                if bfs(row-1, col, word_idx+1):
                    return True
            if row+1 < m and board[row+1][col] == word[word_idx+1] and (row+1, col) not in visited:
                if bfs(row+1, col, word_idx+1):
                    return True
            if col-1 >= 0 and board[row][col-1] == word[word_idx+1] and (row, col-1) not in visited:
                if bfs(row, col-1, word_idx+1):
                    return True
            if col+1 < n and board[row][col+1] == word[word_idx+1] and (row, col+1) not in visited:
                if bfs(row, col+1, word_idx+1):
                    return True
            
            visited.remove((row, col))
        
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                if letter == word[0] and bfs(i, j, 0):
                    return True
        
        return False