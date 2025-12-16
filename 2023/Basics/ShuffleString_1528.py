# Status: Not Bad

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        slen = len(s)
        answ = [""]*slen
        for idx, val in enumerate(s):
            answ[indices[idx]] = val
        return "".join(answ)

solve = Solution()
print(solve.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
