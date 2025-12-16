class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        DP = [[0]*len(text2) for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    DP[i][j] = (DP[i - 1][j - 1] if i-1>=0 and j-1>=0 else 0) + 1
                else:
                    DP[i][j] = max(DP[i - 1][j] if i-1>=0 else 0, DP[i][j - 1] if j-1>=0 else 0)
        return DP[-1][-1]

sol = Solution().longestCommonSubsequence

print(sol(text1 = "oxcpqrsvwf", text2 = "shmtulqrypy"))
print(sol(text1 = "abcde", text2 = "ace"))
print(sol(text1 = "abc", text2 = "abc"))
print(sol(text1 = "xyzabcde", text2 = "xyzace"))  
print(sol(text1 = "qqqqxyzabcde", text2 = "qqqqxyzace"))  
