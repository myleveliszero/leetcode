class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap = dict()
        for i in range(len(s)):
            if s[i] in hmap and hmap[s[i]] != t[i]:
                return False
            if s[i] not in hmap and t[i] in hmap.values():
                return False
            hmap[s[i]] = t[i]
        return True