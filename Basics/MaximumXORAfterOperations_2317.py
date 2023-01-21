# Status: Bad

class Solution:
    def maximumXOR(self, nums: list[int]) -> int:
        answ = 0
        for i in nums:
            answ |= i
        return answ

solve = Solution()
print(solve.maximumXOR(nums = [3,2,4,6]))
print(solve.maximumXOR(nums = [1,2,3,9,2]))