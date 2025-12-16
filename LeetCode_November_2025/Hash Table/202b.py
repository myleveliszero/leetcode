class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            digitSum = 0
            while n:
                digitSum += (n%10)**2
                n //= 10
            n = digitSum
            if n == 1:
                return True
        return False
            

sol = Solution().isHappy
print(sol(2**31-1))            
            