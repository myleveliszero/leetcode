# Status: Good

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diffbit = start^goal
        answ = 0
        while(diffbit):
            diffbit &= diffbit-1
            answ +=1
        return answ
    def version2(self, start, goal):
        return (start^goal).bit_count()

solve = Solution()
print(solve.minBitFlips(4, 8))
print(solve.version2(4, 8))