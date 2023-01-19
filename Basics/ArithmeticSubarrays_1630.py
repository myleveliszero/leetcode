# Status: Not Bad

class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        answ = [True]*len(l)
        for i in range(len(l)):
            subarr = sorted(nums[l[i]:r[i]+1])
            d = subarr[1]-subarr[0]
            for j in range(1,len(subarr)-1):
                if subarr[j+1] - subarr[j] != d:
                    answ[i] = False
                    break
        return answ

solve = Solution()
print(solve.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))