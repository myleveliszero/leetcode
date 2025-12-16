from typing import*
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = 3, 3
        for row in board:
            hset = set()
            for val in row:
                if val != '.':
                    if val in hset:
                        return False
                    hset.add(val)
        for col in range(len(board[0])):
            hset = set()
            for row in range(len(board)):
                val = board[row][col]
                if val != '.':
                    if val in hset:
                        return False
                    hset.add(val)

        for i in range(0, n*m, n):
            for j in range(0, n*m, m):
                hset = set()
                for col in range(n):
                    for row in range(m):
                        val = board[i+row][j+col]
                        if val != '.':
                            if val in hset:
                                return False
                            hset.add(val)
        
        return True 

sol = Solution().isValidSudoku
print(sol([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
