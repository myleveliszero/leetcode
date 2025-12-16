# Status: Good

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = []
        for i in s:
            if i not in visited:
                visited.append(i)
            else:
                return i

solve = Solution()
print(solve.repeatedCharacter(s = "abccbaacz"))
       