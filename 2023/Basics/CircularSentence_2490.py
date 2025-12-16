# Status: Not Bad

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] == sentence[-1]:
            for i in range(len(sentence)):
                if sentence[i] == ' ':
                    if sentence[i+1] != sentence[i-1]:
                        return False
            return True

        else:
            return False

solve = Solution()
print(solve.isCircularSentence(sentence = "leetcode exercises sound delightful"))
print(solve.isCircularSentence(sentence = "Leetcode is cool"))
print(solve.isCircularSentence(sentence = "eetcode"))