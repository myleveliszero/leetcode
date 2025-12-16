from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = dict()
        max_val, cur = 0, 0
        for i in range(len(s)):
            if s[i] in hmap:
                if i-cur > max_val:
                    max_val = i-cur
                if cur <= hmap[s[i]]:
                    cur = hmap[s[i]]+1
            hmap[s[i]] = i
        
        if len(s)-cur > max_val:
            return len(s)-cur

        return max_val

sol = Solution().lengthOfLongestSubstring
print(sol(s="abbbhelloworldhowareyoudoing me fine is asdf9251"))
print(sol(s="abcabcbb"))
print(sol(s="bbbbb"))
print(sol(s="abcdecabg"))
print(sol("ohomm"))
print(sol("bbtablud"))

# # s = "cbdaexzy"
# s = "abcde"
# hmap = dict()
# for i in range(len(s)):
#     hmap[s[i]] = i
# for key in list(hmap.keys())[:hmap['c']]:
#     print(key)
#     hmap.pop(key)
# print(hmap)
