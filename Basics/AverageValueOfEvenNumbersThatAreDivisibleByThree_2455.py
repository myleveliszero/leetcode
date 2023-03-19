# Status: Not Bad

class Solution:
    def averageValue(self, nums: list[int]) -> int:
        avg = []
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                avg.append(i)
        if (len(avg) == 0):
            return 0
        else:
            return int(sum(avg)/(len(avg)))

solve = Solution()
print(solve.averageValue(nums = [1,3,6,10,12,15]))
print(solve.averageValue([1,3,6,10,12,15,16,24,32,36,82,96]))
