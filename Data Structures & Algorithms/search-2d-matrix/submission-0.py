class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top, bottom = 0, ROWS-1

        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row-1
            elif target > matrix[row][-1]:
                top = row+1
            else:
                break
        
        if not (target >= matrix[row][0] and target <= matrix[row][-1]):
            return False
        
        left, right = 0, COLS-1

        while left <= right:
            col = (left + right) // 2
            if target < matrix[row][col]:
                right = col-1
            elif target > matrix[row][col]:
                left = col+1
            else:
                return True
        
        return False

# Binary search over rows then binary search over cols


        # for i in range(length):
        #     if target >= matrix[i][0] and target <= matrix[i][width-1]:
        #         for j in range(width):
        #             if target == matrix[i][j]:
        #                 return True
        #         return False
        
        # return False
