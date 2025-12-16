# Status: Good

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [idx for idx, val in enumerate(sorted(nums)) if val == target]
    def version2(self, nums, target):
        equal, less = 0, 0 
        for n in nums:
            if n == target:
                equal += 1
            elif n < target:
                less +=1
        return range(less, less+equal)

solve = Solution()
print(solve.targetIndices(nums = [1,2,5,2,3], target = 2))
print(solve.version2(nums = [1,2,5,2,3], target = 2))