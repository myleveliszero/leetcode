# Status Good

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxansw = 0
        for sts in sentences:
            curmax = 1
            for j in sts:
                if j == " ":
                    curmax += 1
            if curmax > maxansw:
                maxansw = curmax
        return maxansw
    def version2(self, sentences):
        return max([len(sts.split()) for sts in sentences])
                
solve = Solution()
print(solve.mostWordsFound(sentences = ["alice and bob love leetcode", "i think so too",
 "this is great thanks very much"]))
print(solve.version2(sentences = ["alice and bob love leetcode", "i think so too",
 "this is great thanks very much"]))