# #didn't solved yet

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         left, max_len = 0, 0
#         cur_k = k
#         hmap = dict()
#         for i in range(len(s)):
#             if s[i] not in hmap:
#                 hmap[s[i]] = 0

#             hmap[s[i]] += 1

#             if s[left] != s[i]:
#                 cur_k -= 1
#                 while cur_k < 0:
#                     hmap[s[left]] -= 1
#                     left += 1
#                     total = i-left+1
#                     cur_k = k - (total - hmap[s[left]])
            
#             max_len = max(max_len, i-left+1)
        
#         return max_len

# sol = Solution().characterReplacement
# print(sol("CCBCAABCBACCC", 3) == 7)
# # print(sol("CCCCBAAACBCBCABAABC", 2) == 6)
# # print(sol("BACACCCBBBBBBACCCA", 3) == 9)
# # print(sol("ABABABBAAABBBABAABBAABABABAA", 8) == 18)
# # print(sol("BAABABBBABBBABAABBABAAB", 0) == 3)
# # print(sol("BAAABABAABBBAABBAAAAABABBBBBAABABABBBBABA", 3) == 11)

# from string import ascii_uppercase
# import random as r

# def test(func1):
#     n = r.randrange(10, 20)
#     s = "".join(r.choice(ascii_uppercase[:3]) for _ in range(n))
#     k = r.randrange(0,n//2)
#     # res = func1(s, k)
#     # print("res---: ", res)
#     print(s)
#     print("k-----: ",k)

# # for i in range(10):
# #     test(sol)