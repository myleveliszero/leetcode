# Status: Bad

class Solution:
    def sortSentence(self, s: str) -> str:
        strarr = [""]*9
        word = ""
        for char in s:
            if char in "123456789":
                strarr[int(char)-1] = word
                word = ""
            elif char == " ":
                 continue
            else:
                word += char
        answstr = ""
        for i in strarr:
            if i != "":
                answstr += i + " "
        return answstr


solve = Solution()
print(solve.sortSentence( s = "Myself2 Me1 I4 and3"))
print(solve.sortSentence( s = "pTTy1"))
