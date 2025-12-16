from typing import *
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        firstMax, secondMax = -1, -1
        for idx, val in enumerate(nums):
            if val > firstMax:
                firstMax = val
                maxIdx = idx
            elif val > secondMax:
                secondMax = val
        
        if secondMax == 0:
            return maxIdx
        elif secondMax != 0 and firstMax//secondMax >= 2:
            return maxIdx
        return -1
    
sol = Solution().dominantIndex
print(sol(nums = [3,6,1,0]))
print(sol(nums = [1,2,3,4]))
        