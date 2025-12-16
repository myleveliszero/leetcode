from typing import *
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        opeartions = 0
        res = [1]*(rowIndex+1)
        if rowIndex < 2: return res
        for curRowIdx in range(2, rowIndex+1):
            val = 1
            for i in range(1, curRowIdx):
                res[i], val = res[i]+val, res[i]
                opeartions += 1
        # print("------------operations: ", opeartions)
        return res

sol = Solution().getRow
print(sol(30))
print(sol(20))
print(sol(10))