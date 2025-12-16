from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if  obstacleGrid[ROWS-1][COLS-1] == 1 or \
            obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[ROWS-1][COLS-1] = "1"
        for row in reversed(range(ROWS)):
            for col in reversed(range(COLS)):
                if (row == ROWS-1 and col==COLS-1) or \
                    obstacleGrid[row][col] == 1:
                    continue
                down, right = "0", "0"
                if row+1 != ROWS:
                    down = obstacleGrid[row+1][col]
                    if down == 1:
                        down = "0"
                if col+1 != COLS:
                    right = obstacleGrid[row][col+1]
                    if right == 1:
                        right = "0"
                obstacleGrid[row][col] = str(int(down)+int(right))
                
        return int(obstacleGrid[0][0])
    
sol = Solution().uniquePathsWithObstacles
# print(sol(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
# print(sol(obstacleGrid = [[0,0,0],[0,0,0],[0,0,0]]))
# print(sol(obstacleGrid = [[0,1],[0,0]]))

from random import randrange as rd
from random import choice 
def test(func1=None):
    m, n = rd(1, 20), rd(1,20)
    # grid = [[0]*n]*m
    grid = [[0]*n for _ in range(m)]
    nums = [0]*9
    nums.append(1)
    for row in range(m):
        for col in range(n):
            grid[row][col] = choice(nums)
    
    print("\n------------------Original grid---------------------\n")
    print(grid)
    res = func1(grid)
    print("res: ", res)
    # print("\n------------------Changed grid---------------------\n")

    # print(m,n)
    # for row in grid:
    #     print(*row)


for _ in range(10):
    test(sol)
