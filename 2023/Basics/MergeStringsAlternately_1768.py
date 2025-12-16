# Status: Good

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans, w1len, w2len = "", len(word1), len(word2)
        i = 0
        while i < w1len and i < w2len:
            # ans += word1[i] + word2[i]
            ans += word1[i]
            ans += word2[i]
            i += 1
        if w1len > w2len:
            return ans + word1[i:]
        elif w1len < w2len:
            return ans + word2[i:]
        else:
            return ans
    def version2(self, w1, w2):
        import itertools
        return ''.join(a + b for a, b in itertools.zip_longest(w1, w2, fillvalue=''))

solve = Solution()
print(solve.mergeAlternately(word1 = "abc", word2 = "pqr"))
print(solve.mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(solve.mergeAlternately(word1 = "abcd", word2 = "pq"))
print(solve.version2(w1 = "ab", w2 = "pqrs"))
print(solve.version2(w1 = "abcd", w2 = "pq"))