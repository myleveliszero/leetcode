class Solution:
    def isHappy(self, n: int) -> bool:
        def getNextNum(n):
            digitSum = 0
            while n:
                digitSum += (n%10)**2
                n //= 10
            return digitSum
        def getTwoNextNum(n):
            return getNextNum(getNextNum(n))
        
        slow, fast = n, getTwoNextNum(n)
        while slow != fast:
            slow = getNextNum(slow)
            fast = getTwoNextNum(fast)
        
        return fast == 1

        
            

sol = Solution().isHappy
print(sol(2**31-1))            
            