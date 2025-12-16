class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        def check(sequence, word):
            for idx in range(len(sequence)):
                if sequence[idx] == word[0]:
                    i, j = idx, 0
                    while   (i < len(sequence) and j < len(word)) \
                            and sequence[i] == word[j]:
                        i += 1
                        j += 1
                    if j == len(word):
                        return True            
            return False

        count, w = 0, word
        while check(sequence, w):
            w += word
            count += 1 
        return count                
    


                    