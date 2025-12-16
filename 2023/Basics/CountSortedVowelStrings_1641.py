# Status: Bad

import math

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n+4,4)

solve = Solution()
print(solve.countVowelStrings(33))
print(solve.countVowelStrings(2))