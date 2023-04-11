# Status: Not Bad


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        u = list(set(s))
        n = s.count(u[0])
        for i in range(1, len(u)):
            if n != s.count(u[i]):
                return False
        return True

solve = Solution()
print(solve.areOccurrencesEqual(s = "abacbc"))

print(solve.areOccurrencesEqual(s = "aaabb"))  