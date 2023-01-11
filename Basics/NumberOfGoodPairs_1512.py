# Status: Not Bad

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        nlen = len(nums)
        answ = 0
        for i in range(nlen):
            for j in range(i+1, nlen):
                if nums[i] == nums[j]:
                    answ += 1
        return answ

solve = Solution()
print(solve.numIdenticalPairs([1,2,3,1,1,3]))