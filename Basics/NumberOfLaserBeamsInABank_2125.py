# Status: 

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        answ = 0
        sequence = []
        for row in bank:
            count = row.count('1')
            if count:
                sequence.append(count)
        for i in range(len(sequence)-1):
            answ += sequence[i]*sequence[i+1]
        return answ
    def version2(self, bank):
        answ, prev = 0, 0
        for row in bank:
            beams = row.count("1")
            if beams:
                answ += prev*beams
                prev = beams
        return answ

solve = Solution()
print(solve.numberOfBeams( bank = ["011001","000000","010100","001000"]))
print(solve.version2( bank = ["011001","000000","010100","001000"]))