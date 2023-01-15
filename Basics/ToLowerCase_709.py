# Status: Good

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
    def version2(self, s):
        answ = ""
        for char in s:
            if ord(char) < 90:
                answ += chr(ord(char)+32)
            else:
                answ += char
        return answ

solve = Solution()
print(solve.toLowerCase("Hello"))
print(solve.version2("Hello"))
print(solve.toLowerCase("LOVELY"))
print(solve.version2("LOVELY"))