from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for val in nums:
            if val in hashset:
                return True
            hashset.add(val)
        return False
    
