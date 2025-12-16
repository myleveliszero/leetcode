# Status: Good

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                cnt += 1
            if s[i] == ' ':
                if cnt != 0:
                    return cnt
        return cnt
    def simple(self, s):
        return len((s.split())[-1])
    
solve = Solution()
print(solve.lengthOfLastWord(s = "   fly me   to   the moon  "))
print(solve.simple(s = "   fly me   to   the moon  "))