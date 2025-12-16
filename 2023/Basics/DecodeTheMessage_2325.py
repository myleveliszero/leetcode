# Status: Good

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        unique = {}
        count = 97
        for letter in key:
            if letter in unique or letter ==" ":
                continue
            unique[letter] = chr(count)
            count += 1
        unique[" "] = " "
        answ = ""
        for char in message:
            answ += unique[char]
        return answ


solve = Solution()
print(solve.decodeMessage( key = "the quick brown fox jumps over the lazy dog", 
message = "vkbs bs t suepuv"))
print(solve.decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", 
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))
