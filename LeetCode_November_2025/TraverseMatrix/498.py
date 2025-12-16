from typing import *
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up, down = True, False
        upBegin, downBegin = True, False
        i,j,m,n = 0,0,len(mat), len(mat[0])
        res = []
        while i < m and j < n:
            if upBegin:
                upBegin = False
                res.append(mat[i][j])
            elif up and (i-1 >= 0 and j+1<n):
                i, j = i-1, j+1
                res.append(mat[i][j])
            elif up:
                up, down = False, True
                if j+1 < n:
                    j += 1
                else:
                    i += 1
                downBegin = True
            elif downBegin:
                downBegin = False
                res.append(mat[i][j])
            elif down and (i+1 < m and j-1 >= 0):
                i, j = i+1, j-1
                res.append(mat[i][j])
            elif down:
                up, down = True, False
                if i+1 < m:
                    i += 1
                else:
                    j += 1
                upBegin = True
                        
        return res


sol = Solution().findDiagonalOrder
print(sol(mat = [[1,2],[3,4]]))
print(sol([[1,2],[4,5],[7,8]]))
print(sol([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],]))