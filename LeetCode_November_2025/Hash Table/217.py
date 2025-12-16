from typing import *
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return not (len(set(nums)) == len(nums))
        hashset= set()
        for val in nums:
            if val not in hashset:
                hashset.add(val)
            else:
                return True
        return False