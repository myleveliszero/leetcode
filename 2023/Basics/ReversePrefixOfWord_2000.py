# Status: Good

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i+1][::-1] + word[i+1:]
        return word
    def version2(self, word, ch):
        answ = ""
        cut = False
        for idx, val in enumerate(word):
            answ = val + answ
            if val == ch:
                cut = idx + 1
                break
        if cut:
            return answ + word[cut:]
        else:
            return word
                

solve = Solution()
print(solve.reversePrefix(word = "abcdefd", ch = "d"))
print(solve.reversePrefix(word = "xyxzxe", ch = "z"))
print(solve.reversePrefix(word = "abcd", ch = "z"))
print(solve.version2(word = "abcdefd", ch = "d"))
print(solve.version2(word = "abcd", ch = "z"))