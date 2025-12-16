from typing import *
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = 0, n
        res = [0]*2*n
        cur = 0
        while right < 2*n:
            res[cur] = nums[left]
            cur += 1
            res[cur] = nums[right]
            cur += 1
            left, right = left+1, right+1
        
        return res