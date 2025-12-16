from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for idx, val in enumerate(nums):
            if val in hmap:
                if val*2==target:
                    return [idx, hmap[val]]
            else:
                hmap[val] = idx
        
        for key in hmap.keys():
            if 2*key != target and (target-key) in hmap:
                return [hmap[key], hmap[target-key]]
        
sol = Solution().twoSum
print(sol(nums = [2,7,11,15], target = 9))