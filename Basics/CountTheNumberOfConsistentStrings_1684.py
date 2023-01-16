# Status: Good

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        answ = 0 
        for word in words:
            count = 1
            for char in word:
                if char not in allowed:
                    count = 0
                    break
            answ += count
        return answ

solve = Solution()
print(solve.countConsistentStrings(allowed = "ab", 
words = ["ad","bd","aaab","baa","badab"]))