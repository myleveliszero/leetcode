# Status: Not Bad

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        firstrow = "qwertyuiop"
        secondrow = "asdfghjkl"
        thirdrow = "zxcvbnm"
        ans = []
        for word in words:
            f = s = t = True
            lword = word.lower() 
            for i in lword:
                if i not in firstrow:
                    f = False
                if i not in secondrow:
                    s = False
                if i not in thirdrow:
                    t = False
            if f:
                ans.append(word)
            elif s:
                ans.append(word)
            elif t:
                ans.append(word)
        return ans

solve = Solution()
print(solve.findWords(words = ["Hello","Alaska","Dad","Peace"]))

print(solve.findWords( words = ["omk"]))

print(solve.findWords( words = ["adsdf","sfd"]))