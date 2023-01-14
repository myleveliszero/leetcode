# Status: Good

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        answ = []
        for i in sentence:
            if i not in answ:
                answ.append(i)
        return len(answ) == 26
    def version2(self, sentence):
        alpha = "qwertyuiopasdfghjklzxcvbnm"
        count = 0
        for i in range(len(alpha)):
            if alpha[i] not in sentence:
                return False

        return True
    def version3(self, sentence):
        return len(set(sentence)) == 26

solve = Solution()
print(solve.checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))
print(solve.checkIfPangram(sentence = "leeetcoodeee"))
print(solve.version2(sentence = "thequickbrownfoxjumpsoverthelazydog"))
print(solve.version2(sentence = "leeetcoodeee"))
print(solve.version3(sentence = "leeetcoodeee"))
print(solve.version3(sentence = "thequickbrownfoxjumpsoverthelazydog"))