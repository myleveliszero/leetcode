# Status: Not Bad

class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while nums:
            nlen = len(nums)
            
            if nlen == 1: break

            newNums = [0]*(nlen-1)
            for i in range(nlen-1):
                newNums[i] = (nums[i] + nums[i+1]) % 10
            nums = newNums
        return nums[0]


solve = Solution()
print(solve.triangularSum(nums = [1,2,3,4,5]))