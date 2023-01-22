# Status: Good

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {
            "a": 1,"e": 1,"i": 1,"o": 1,"u": 1,
            "A": 1,"E": 1,"I": 1,"O": 1,"U": 1,
        }
        half = len(s)//2
        left, right = s[:half], s[half:]
        cnt = 0
        for i in range(half):
            cnt += vowels.get(left[i], 0) - vowels.get(right[i], 0)
        return cnt == 0
    
    def version2(self, s):
        s = s.lower()
        a = s[:(len(s)//2)]
        b = s[(len(s)//2):]
        cnt = 0
        for i in range(len(a)):
            if a[i] in "aeiou":
                cnt +=1
            if b[i] in "aeiou":
                cnt -=1
        return cnt == 0

solve = Solution()
print(solve.halvesAreAlike(s = "book"))
print(solve.halvesAreAlike(s = "textbook"))
print(solve.version2(s = "book"))
print(solve.version2(s = "textbook"))