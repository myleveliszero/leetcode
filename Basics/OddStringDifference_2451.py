# Status: Not Bad

class Solution:
    def oddString(self, words: list[str]) -> str:
        ans = []
        for w in words:
            temp = []
            for i in range(0, len(w)-1):
                temp.append(ord(w[i+1])-ord(w[i]))
            ans.append(temp)

        for i in range(1, len(ans)):
            if ans[0] != ans[i]:
                if i == 1:
                    if ans[i+1] == ans[i]:
                        return words[0]
                    else:
                        return words[1]
                else:
                    return words[i]

solve = Solution()
print(solve.oddString(words = ["adc","wzy","abc"]))