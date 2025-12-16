# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:        
#         def dfs(text1, text2, idx1, idx2, visit):
#             if idx1 >= len(text1) or idx2 >= len(text2):
#                 return len(visit) if visit else 0
            
#             if text1[idx1] == text2[idx2]:
#                 visit.append(text1[idx1])
#                 idx1, idx2 = idx1+1, idx2+1
#                 val1 = dfs(text1, text2, idx1, idx2, visit)
#                 visit.pop()
#                 return val1

#             val2 = dfs(text1, text2, idx1, idx2+1, visit)
#             val3 = dfs(text1, text2, idx1+1, idx2, visit)
            
#             return  val2 if val2 > val3 else val3
        
#         res = dfs(text1, text2, 0, 0, [])

#         return res

# sol = Solution().longestCommonSubsequence

# print(sol(text1 = "abccde", text2 = "acce"))
# print(sol(text1 = "pkaokgmaqewfhtzcqdkevptkktyxwggnpmqsrngvfxwmrcpnvatpoootnrpvpwnyoqebsbwkqtavljskjtcfysaj", 
#           text2 = "sqxnqhkexggwtjkkmohtkjknmfzahuogqxpdwrvqzmcgwczdwmdgwskigrulhalnc"))
# print(sol(text1 = "abcde", text2 = "ace"))
# print(sol(text1 = "abc", text2 = "abc"))
# print(sol(text1 = "xyzabcde", text2 = "xyzace"))  
# print(sol(text1 = "qqqqxyzabcde", text2 = "qqqqxyzace"))  
# 2
# 3
# 3
# 6
# 10