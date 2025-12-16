from typing import * 
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            hmap[key].append(s)

        return list(hmap.values())
    
sol = Solution().groupAnagrams
print(sol(strs = ["eat","tea","tan","ate","nat","bat"]))