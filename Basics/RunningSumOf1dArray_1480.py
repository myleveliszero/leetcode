# Status: Good(99/100)

import itertools
import operator

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
    
    def version2(self, nums):
        return itertools.accumulate(nums, operator.add)

solve = Solution()
print(solve.runningSum([1,2,3,4,5,6,7,8,9]))
print(solve.runningSum([1,1,2,2]))
answ = solve.version2([1,2,3,4,5,6,7,8,9])
print(answ)
for i in answ: print(i, end=" ") 
print('')