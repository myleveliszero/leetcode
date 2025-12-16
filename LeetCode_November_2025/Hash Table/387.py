class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = dict()
        for i in range(len(s)):
            if s[i] in hmap:
                hmap[s[i]] = len(s)
            else:
                hmap[s[i]] = i

        for key in hmap.keys():
            if hmap[key] != len(s):
                return hmap[key]
        
        return -1
    
sol = Solution().firstUniqChar
# print(sol(s = "leetcode"))
# print(sol(s = "loveleetcode"))
# print(sol(s = "aabb"))
# print(sol(s = "ab"))
print(sol(s = "babasf"))