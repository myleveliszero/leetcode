from typing import *
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        leftEnd, rightEnd = 0, n-1
        upEnd, downEnd = 0, m-1
        right, down, left, up = True, False, False, False
        i, j = 0, 0
        res = []
        while len(res)+1<m*n:
            if right and j+1 <= rightEnd:
                res.append(matrix[i][j])
                j += 1
            elif right:
                right, down = False, True
                rightEnd -= 1
            elif down and i+1 <= downEnd:
                res.append(matrix[i][j])
                i += 1
            elif down:
                down, left = False, True
                downEnd -= 1
            elif left and j-1 >= leftEnd:
                res.append(matrix[i][j])
                j -= 1
            elif left:
                left, up = False, True
                leftEnd += 1
            elif up and i-1 > upEnd:
                res.append(matrix[i][j])
                i -= 1
            elif up:
                up, right = False, True
                upEnd += 1
        res.append(matrix[i][j])
        return res
    

sol = Solution().spiralOrder

print(sol(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(sol(matrix = [[1,2],[3,4]]))
print(sol([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]))

# print(sol([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))
# print(sol( matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))