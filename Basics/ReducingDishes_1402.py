# Status: Not Bad

class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        ans = 0
        for i in range(len(satisfaction)):
            cursum = 0
            for j in range(len(satisfaction)-i):
                cursum += (j+1)*satisfaction[j+i]
            if cursum > ans:
                ans = cursum 
        return ans

solve = Solution()
print(solve.maxSatisfaction(satisfaction =[-1,-8,0,5,-7]))
print(solve.maxSatisfaction(satisfaction =[4,3,2]))