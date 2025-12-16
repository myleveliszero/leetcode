class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap = dict()
        hmap2 = dict()
        for i in range(len(s)):
            if s[i] in hmap and hmap[s[i]] != t[i]:
                return False
            if t[i] in hmap2 and hmap2[t[i]] != s[i]:
                return False
            hmap[s[i]] = t[i]
            hmap2[t[i]] = s[i]
        return True

sol = Solution().isIsomorphic
print(sol( s = "egg", t = "add"))
print(sol( s = "foo", t = "bar"))
print(sol( s = "badc", t = "baba"))
print(sol( s = "foo", t = "boo"))
print(sol( s = "foo", t = "saa"))
 
 