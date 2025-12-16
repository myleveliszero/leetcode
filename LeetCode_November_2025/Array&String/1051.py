from typing import *
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        cnt = 0
        for one, two in zip(heights, exp):
            if one != two:
                cnt += 1
        return cnt 
    
sol = Solution().heightChecker
print(sol(heights = [1,1,4,2,1,3]))


    