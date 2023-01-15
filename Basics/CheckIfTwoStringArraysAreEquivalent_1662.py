# Status: Good

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        i, n = 0, 0
        j, m = 0, 0 
        w1len = len(word1)
        w2len = len(word2)
        while (i < w1len and j <w2len):
            if word1[i][n] != word2[j][m]:
                return False
            n, m = n+1, m+1
            if n >= len(word1[i]):
                i, n = i+1, 0
            if m >= len(word2[j]):
                j, m = j+1, 0
            
        return i == w1len and j == w2len
        

    def version2(self, word1, word2):
        s1 = ""
        for char in word1:
            s1 += char
        s2 = ""
        for char in word2:
            s2 += char
        slen1 = len(s1)
        slen2 = len(s2)
        if slen1 != slen2: return False

        for i in range(slen1):
            if s1[i] != s2[i]:
                return False
        return True
    def version3(self, word1, word2):
        return "".join(word1) == "".join(word2)
                


solve = Solution()
print(solve.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print(solve.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
print(solve.version2(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print(solve.version2(word1 = ["a", "cb"], word2 = ["ab", "c"]))
print(solve.version3(word1 = ["abc","d","defg"], word2 = ["abcddef"]))
