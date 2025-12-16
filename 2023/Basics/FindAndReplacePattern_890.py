# Status: Good

import collections

class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def find_pattern(s: str):
            unique = collections.defaultdict() 
            val, res = 0, []
            for ch in s:
                if ch not in unique:
                    val += 1
                    unique[ch] = val
                res.append(unique[ch])
            return res

        P = find_pattern(pattern)
        return [s for s in words if P==find_pattern(s)]


solve = Solution()
print(solve.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))