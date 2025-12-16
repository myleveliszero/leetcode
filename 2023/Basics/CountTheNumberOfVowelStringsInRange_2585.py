# Status: Not Bad

class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        cnt = 0
        for i in range(left, right+1):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                cnt +=1
        return cnt

solve = Solution()
print(solve.vowelStrings(words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4))