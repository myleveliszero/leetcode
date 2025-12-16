from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def fresh_or_out_boundaries(grid, row, col, visit):
            if  min(row, col) < 0 or row==ROWS or col==COLS \
                or (row, col) in visit or grid[row][col] != 2:
                return True
            return False
        def empty_or_out_boundaries(grid, row, col, visit):
            if  min(row, col) < 0 or row==ROWS or col==COLS \
                or (row, col) in visit or grid[row][col] == 0:
                return True
            return False

        ROWS, COLS = len(grid), len(grid[0])
        q, visit = list(), set()
        lst = []
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    lst.append((row,col))
        q.append(lst)
        minute = 0
        while q:
            cur = q.pop()
            nxt = list()
            fresh_detected = False
            for row, col in cur:
                if  fresh_or_out_boundaries(grid, row, col, visit):
                    continue
                
                for rowss in grid:
                    print(*rowss)
                print("-----------------")
                visit.add((row, col))
                neighbours = [(-1,0),(1,0),(0,-1),(0,1)]
                for dr, dc in neighbours:
                    if  not empty_or_out_boundaries(grid, row+dr, col+dc, visit):
                        nxt.append((row+dr, col+dc))
                        if grid[row+dr][col+dc] == 1:
                            fresh_detected = True
                            grid[row+dr][col+dc] = 2

            if nxt:
                q.append(nxt)
            if not fresh_detected:
                break
            minute += 1
            
       
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1   
        return minute

sol = Solution().orangesRotting

grid1 = [[1,1,1],
         [1,1,0],
         [2,1,1]]

grid2 = [[2,1,1],
         [0,1,1],
         [1,0,1]]

grid3 = [[1],[0],[1]]

print(sol(grid1))
print(sol(grid2))
print(sol(grid3))