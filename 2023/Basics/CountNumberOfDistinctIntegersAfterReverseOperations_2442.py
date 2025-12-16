# Status: Good

class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        answ = set(nums)
        for i in nums:
            answ.add(int(str(i)[::-1]))
        return len(answ)
    def version2(self, nums):
        answ = set(nums)
        for curnum in nums:
            revse = 0
            while curnum:
                revse = (revse*10) +(curnum%10)
                curnum //= 10
            answ.add(revse)
        return len(answ)
solve = Solution()
print(solve.countDistinctIntegers([1,13,10,12,31]))
print(solve.version2([1,13,10,12,31]))