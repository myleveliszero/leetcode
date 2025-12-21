class Solution:
    def lengthOfLongestSubstring_2(self, s: str) -> int:
        hmap = dict()
        left, max_len = 0, 0
        for i in range(len(s)):
            if s[i] in hmap:
                # left = left if left > hmap[s[i]]+1 else hmap[s[i]]+1
                left = max(left, hmap[s[i]]+1)

            hmap[s[i]] = i
            # max_len = max_len if max_len > i-left+1 else i-left+1
            max_len = max(max_len, i-left+1)

        return max_len 


    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap, max_len = dict(), 0
        for i in range(len(s)):
            if s[i] in hmap:
                key = next(iter(hmap))
                hmap.pop(key)
                while hmap and key != s[i]:
                    key = next(iter(hmap))
                    hmap.pop(key)

            hmap[s[i]] = i
            max_len = max(max_len, len(hmap))

        return max_len
    
print(Solution().lengthOfLongestSubstring_2("aabaab!bb"))
print(Solution().lengthOfLongestSubstring_2("dvdf"))
# print(Solution().lengthOfLongestSubstring("aabaab!bb"))
# print(Solution().lengthOfLongestSubstring("dvdf"))
