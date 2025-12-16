from typing import *
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for idx, val in enumerate(nums):
            if idx+1 != val:
                while nums[val-1] != val:
                    nums[val-1], val = val, nums[val-1]

        answ = []
        for idx, val in enumerate(nums):
            if idx+1 != val:
                answ.append(idx+1)
        return answ


sol = Solution().findDisappearedNumbers
print(sol(nums = [4,3,2,7,8,2,3,1])) 