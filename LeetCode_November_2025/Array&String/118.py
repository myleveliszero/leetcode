from typing import *
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        
        for _ in range(numRows-2):
            i, arr = 0, [1]
            while i+1 < len(res[-1]):
                arr.append(res[-1][i]+res[-1][i+1])
                i += 1
            arr.append(1)
            res.append(arr)
        return res
    
sol = Solution().generate
print(sol(5))
print(sol(6))
print(sol(1))