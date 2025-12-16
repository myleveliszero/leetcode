from typing import * 
from collections import defaultdict
# import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')] += 1
            hmap[tuple(key)].append(s)

        return list(hmap.values())
    
sol = Solution().groupAnagrams
# print(sol(strs = ["eat","tea","tan","ate","nat","bat"]))
print(sol(strs = ["duh","ill"]))
