# Status: Not Bad

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        answ = []
        nlen = len(nums)
        for i in range(nlen):
            curnumber = 0
            for  j in range(nlen):
                if i != j and nums[i] > nums[j]:
                    curnumber += 1
            answ.append(curnumber)
        return answ
    def version2(self, nums):
        dicti = {}
        for idx, num in enumerate(sorted(nums)):
            dicti.setdefault(num, idx) 
        print(dicti)
        return [dicti[num] for num in nums]
            

solve = Solution()
print(solve.smallerNumbersThanCurrent([8,6,3,2,4,1,8,9,2]))
print(solve.version2([8,6,3,2,4,1,8,9,2]))
