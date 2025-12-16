# Status: Good

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        answ = 0
        mlen = len(mat)
        for i in range(mlen):
            answ += mat[i][i] + mat[i][~i]
        return answ if mlen%2 == 0 else answ - mat[mlen//2][mlen//2]
    def version2(self, mat):
        answ, mlen = 0, len(mat)
        mid = mlen//2
        for i in range(mid):
            answ += mat[i][i]+mat[i][~i]+mat[~i][~i]+mat[~i][i]  
        return answ if mlen%2 == 0 else answ + mat[mid][mid]

solve = Solution()
print(solve.diagonalSum(mat = [ [1,2,3],
                                [4,5,6],
                                [7,8,9]]))
print(solve.version2(mat = [ [1,2,3],
                                [4,5,6],
                                [7,8,9]]))
                       