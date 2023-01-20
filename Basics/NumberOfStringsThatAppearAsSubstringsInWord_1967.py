# Status: Good

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        """
        if patterns[i] is substring of word: answ += 1
        """
        answ = 0
        for i in patterns: 
            if i in word:  
                answ += 1
        return answ
    def version2(self, patterns, word):
        return sum(pattern in word for pattern in patterns)

solve = Solution()
print(solve.numOfStrings(patterns = ["a","abc","bc","d"], word = "abc"))
print(solve.version2(patterns = ["a","abc","bc","d"], word = "abc"))