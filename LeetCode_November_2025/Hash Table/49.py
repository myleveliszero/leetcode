from typing import * 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = dict()
        for str in strs:
            sstr = ''.join(sorted(str))
            if sstr  in hmap:
                hmap[sstr].append(str)
            else:
                hmap[sstr] = [str]    
        return list(hmap.values())
    
sol = Solution().groupAnagrams
print(sol(strs = ["eat","tea","tan","ate","nat","bat"]))