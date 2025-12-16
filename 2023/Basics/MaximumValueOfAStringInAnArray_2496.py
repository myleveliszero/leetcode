# Status: Not Bad

class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        maxVal = 0
        for i in strs:
            isNumeric = True
            for j in i:
                if 96 < ord(j) < 123:
                    if len(i) > maxVal:
                        maxVal = len(i)
                    isNumeric = False
                    break
            if isNumeric:
                if int(i) > maxVal:
                    maxVal = int(i)
        return maxVal
    
solve = Solution()
print(solve.maximumValue(strs = ["alic3","bob","3","4","00000"]))
