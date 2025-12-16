# Status: Not Bad

class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        r, s = list(set(ranks)), list(set(suits))
        rcnt, scnt = [0]*len(ranks),[0]*len(suits)
        for i in range(len(r)):
            for j in range(len(ranks)):
                if r[i] == ranks[j]:
                    rcnt[i] += 1
        
        for i in range(len(s)):
            for j in range(len(suits)):
                if s[i] == suits[j]:
                    scnt[i] += 1

        smax = max(scnt)
        rmax = max(rcnt)
        if smax == 5:
            return "Flush"
        elif rmax >= 3:
            return "Three of a Kind"
        elif rmax == 2:
            return "Pair"
        else:
            return "High Card"

solve = Solution()
print(solve.bestHand(ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]))