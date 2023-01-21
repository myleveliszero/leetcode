# Status: Good

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            wlen = len(word)//2
            palindromic = True
            for char in range(wlen):
                left = word[char]
                right = word[~char]
                if  left !=  right:
                    palindromic = False
                    break
            if palindromic:
                return word
        return ""
    def version2(self, words):
        for word in words:
            if word == word[::-1]:
                return word
        return ""

solve = Solution()
print(solve.firstPalindrome(words = ["abc","car","ada","racecar","cool"]))
print(solve.firstPalindrome(words = ["notapalindrome","racecar"]))
print(solve.firstPalindrome(words = ["notapalindrome","racakaacar"]))
print(solve.version2(words = ["notapalindrome","racecar"]))
print(solve.version2(words = ["abc","car","ada","racecar","cool"]))