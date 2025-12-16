# Status: Not Bad

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        idx = 1
        forward = True
        for i in range(time):
            if (idx+1 > n):
                forward = False
            if not forward:
                if (idx-2 == -1):
                    forward = True
            
            if forward:
                idx += 1
            else:
                idx -= 1
        return idx

solve = Solution()
print(solve.passThePillow(4,5))
print(solve.passThePillow(1000,1000))