from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hset = set()
        for val in nums:
            if val in hset:
                hset.remove(val)
            else:
                hset.add(val)
        return list(hset)[0]