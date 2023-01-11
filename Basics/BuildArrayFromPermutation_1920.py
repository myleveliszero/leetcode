# Status: 

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: answ = [0,1,2,4,5,3] = nums[nums[i]], 0 <= i,nums[i] < len
# Input: nums = [0,3,1,2]
# Output: [0,2,3,1]

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
       return [nums[i] for i in nums]

solve = Solution()
print(solve.buildArray([0,2,4,3,1]))
print(solve.buildArray([1,0]))

