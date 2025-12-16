# Status: Not Bad


class Solution:
    def partitionString(self, s: str) -> int:
        empty = ''
        cnt = 1
        for i in range(len(s)):  
            if s[i] in empty:
                cnt += 1
                empty = s[i]
            else:
                empty += s[i]
        return cnt
    
solve = Solution()
print(solve.partitionString("cuieokbs"))
print(solve.partitionString("abacaba"))
print(solve.partitionString("ssssss"))
print(solve.partitionString("gizfdfri"))