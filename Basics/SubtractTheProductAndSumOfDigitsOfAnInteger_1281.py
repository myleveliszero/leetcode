# Status: Good

import functools
import operator

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        sumansw = 0
        prodansw = 1
        for i in n:
            sumansw += int(i)
            prodansw *= int(i)
        return prodansw-sumansw
    def version2(self, n):
        nprod, nsum = 1,0 
        while n: 
            i = n%10
            nprod *= i
            nsum += i
            n //= 10
        return nprod - nsum
    def version3(self, n):
        digits = [int(i) for i in str(n)]
        return functools.reduce(operator.mul, digits) - sum(digits)

solve = Solution()
print(solve.subtractProductAndSum(356))
print(solve.version2(356))
print(solve.version3(234))