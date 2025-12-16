from typing import List
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q, visit = list(), set()
        length = 1
        row, col = 0, 0 
        q.append([(row,col)])
        while q:
            cur_layer = q.pop()
            next_layer = list()
            for row, col in cur_layer:
                if  min(row, col) < 0 or row == ROWS or col == COLS \
                    or grid[row][col] == 1 or (row,col) in visit:
                    continue
                
                if row == ROWS-1 and col == COLS-1:
                    return length
                
                visit.add((row,col))
                neigbours = [(1, 0),(-1, 0),(0, 1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
                for dr, dc in neigbours:
                    next_layer.append((row+dr,col+dc))
            
            if next_layer:
                q.append(next_layer)            
            
            length += 1

        return -1



        
            

sol = Solution().shortestPathBinaryMatrix

grid1 = [[0,1],
         [1,0]]

grid2 =[[0,0,0],
        [0,1,1],
        [0,0,0]]

grid3 = [[0]]

print(sol(grid1))
print(sol(grid2))
print(sol(grid3))