# Status: Good

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def unique_s(s, t):
            res = s + t
            uniq = ""
            for i in res:
                if i not in uniq:
                    uniq += i
            return uniq
        allchars = unique_s(s,t)
        scnt, tcnt = [], []
        for ch in allchars:
            scnt.append(s.count(ch, 0))
            tcnt.append(t.count(ch, 0))
        answ  = 0
        for i in range(len(scnt)):
            if scnt[i] - tcnt[i] > 0:
                answ += scnt[i]-tcnt[i]
        return answ
    def version2(self, s, t):
        sunique = set([*s])
        scnt, tcnt = [], []
        for ch in sunique:
            scnt.append(s.count(ch))
            tcnt.append(t.count(ch))
        answ  = 0
        for idx in range(len(scnt)):
            if scnt[idx] - tcnt[idx] > 0:
                answ += scnt[idx]-tcnt[idx]
        return answ

         

solve = Solution()
print(solve.minSteps(s = "bab", t = "aba"))
print(solve.minSteps(s = "leetcode", t = "practice"))
print(solve.minSteps(s = "anagram", t = "mangaar"))
print(solve.version2(s = "bab", t = "aba"))
print(solve.version2(s = "leetcode", t = "practice"))
print(solve.version2(s = "anagram", t = "mangaar"))