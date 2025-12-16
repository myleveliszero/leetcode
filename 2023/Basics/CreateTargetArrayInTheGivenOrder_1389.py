# Status: Not Bad

class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        answ = []
        for idx, val in zip(index, nums):
            answ.insert(idx, val)
        return answ
    def version2(self, nums, index):
        answ = []
        for idx, val in zip(index, nums):
            answ[idx:idx] = [val]
        return answ


solve = Solution()
print(solve.createTargetArray(nums = [0,1,2,3,4], index = [2,1,0,2,1]))
print(solve.version2(nums = [0,1,2,3,4], index = [2,1,0,2,1]))
