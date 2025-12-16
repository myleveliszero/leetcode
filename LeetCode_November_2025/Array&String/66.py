from typing import *
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        n  = len(digits)
        answ = [0]*(n+1)
        plusOne = True
        for i in range(n-1,-1,-1):
            if digits[i] == 9 and plusOne:
                answ[i+1] = 0
            elif digits != 9 and plusOne:
                answ[i+1] = digits[i]+1
                plusOne = False
            else:
                answ[i+1] = digits[i]
        
        if plusOne:
            answ[0] = 1
        elif answ[0] == 0:
            return answ[1:]

        return answ
        


sol = Solution().plusOne
print(sol(digits = [4,3,2,1]))
print(sol(digits = [1,9,9]))
print(sol(digits = [9,9,9,9,9]))