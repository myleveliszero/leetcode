# Status: Good

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1
    def version2(self, n):
        answ = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
                answ += n
            else:
                n = (n-1)//2 + 1
                answ += n-1
        return int(answ)
                

solve = Solution()
print(solve.numberOfMatches(25))
print(solve.version2(167))