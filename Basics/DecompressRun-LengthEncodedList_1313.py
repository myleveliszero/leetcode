# Status: Not Bad

class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        answ = []
        for i in range(0, len(nums), 2):
            answ += [nums[i+1]]*nums[i]
        return answ

solve = Solution()
print(solve.decompressRLElist([1,2,3,4]))