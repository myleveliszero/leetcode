# Status: Not Bad


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums)//2):
            if nums[2*i] != nums[2*i+1]:
                return False
        return True

solve = Solution()
print(solve.divideArray( nums = [3,2,3,2,2,2]))
print(solve.divideArray( nums = [1,2,3,4]))