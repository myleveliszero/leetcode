from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for idx, val in enumerate(nums):
            if (target-val) in hashmap:
                return [idx, hashmap[target-val]]
            hashmap[val] = idx
