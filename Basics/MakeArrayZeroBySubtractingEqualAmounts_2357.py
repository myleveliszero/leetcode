# Status: Good

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        if len(nums) == 1 and nums[0] == 0:
            return 0
        else:
            u = set(nums)
            if 0 in u:
                return len(u) -1
            else:
                return len(u)

solve = Solution()
print(solve.minimumOperations([1,5,0,3,5]))

print(solve.minimumOperations([0]))

print(solve.minimumOperations([1,2,3,4,5,6,7,8,9,10]))

print(solve.minimumOperations([1,23,3,4,5,6,7,24,32,8,9,10,23,62]))