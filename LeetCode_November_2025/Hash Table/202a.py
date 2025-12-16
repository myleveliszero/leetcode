class Solution:
    def isHappy(self, n: int) -> bool:
        hset = {n}
        while True:
            sum = 0
            for val in str(n):
                sum += (int(val))**2
            if sum == 1:
                return True
            if sum not in hset:
                hset.add(sum)
                n = sum
            else:
                return False

sol = Solution().isHappy
print(sol(2**31-1))            
            