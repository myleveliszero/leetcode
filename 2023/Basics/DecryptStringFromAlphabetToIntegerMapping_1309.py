# Status: Not Bad

import re

class Solution:
    def freqAlphabets(self, s: str) -> str:
        condtion = re.findall(r'\d\d#|\d', s)
        answ = []
        for char in condtion:
            letter = chr((int(char[:2])+96))
            answ.append(letter)
        return "".join(answ)


solve = Solution()
print(solve.freqAlphabets(s = "10#11#12"))
print(solve.freqAlphabets(s = "1326#"))