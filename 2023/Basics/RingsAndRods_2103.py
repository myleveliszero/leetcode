# Status: Good

class Solution:
    def countPoints(self, rings: str) -> int:
        ninerods = [set() for i in range(10)]
        for i in range(1, len(rings), 2):
            ninerods[int(rings[i])].add(rings[i-1])
        answ = 0
        for i in range(10):
            if len(ninerods[i]) == 3:
                answ += 1
        return answ
            

solve = Solution()
print(solve.countPoints(rings = "B0B6G0R6R0R6G9"))
