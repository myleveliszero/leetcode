# Status: Good

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        answ = ""
        countk = 1
        for char in s:
            if char == " ":
                if countk == k: 
                    break
                countk += 1
            answ += char       
        return answ     
    def version2(self, s, k):
        answidx = 0
        countk1 = 1
        for char in s:
            if char == " ":
                if countk1 == k:
                    break
                countk1 += 1
            answidx += 1
        return s[:answidx]
    def version2point2(self, s, k):
        for idx, val in enumerate(s):
            if val == " ":
                k -= 1
                if k == 0:
                    return s[:idx]
        return s

    def version3(self, s, k):
        return " ".join(s.split(maxsplit=k)[:k])
    
solve = Solution()
print(solve.truncateSentence(s = "Hello how are you Contestant", k = 4))
print(solve.version2(s = "Hello how are you Contestant", k = 4))
print(solve.version3(s = "Hello how are you Contestant", k = 4))
