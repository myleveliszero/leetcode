# Status: Not Bad

class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        zeros = nums.count(0)
        ans = []
        for i in nums:
            if i != 0:
                ans.append(i)
        for i in range(zeros):
            ans.append(0)

        return ans

solve = Solution()
print(solve.applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))
print(solve.applyOperations([1,2,2,1,1,0]))
print(solve.applyOperations([0,1]))