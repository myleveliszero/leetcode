# Status: Not Bad

class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        cnt, wlen, plen = 0, len(words), len(pref)
        for i in range(wlen):
            if len(words[i]) < plen:
                continue
            cnt += 1
            for j in range(plen):
                if pref[j] != words[i][j]:
                    cnt -= 1
                    break
        return cnt
    def version2(self, words, pref):
        ans, plen = 0, len(pref)
        for i in words:
            if plen > len(i):
                continue
            if i[:plen] == pref:
                ans += 1
        return ans


solve = Solution()
print(solve.prefixCount(words =
["kttxeksggb","vucqwew","lyknscc","mryl","vwarnwkfmd","ivawxbntgs","mylw","namybmfy","uosag","rzernqxyn","puf","hfwjnmvm",
"jjfyd","xteybd","v","ywntwzn","npsogop","brgvlw","vewhi","brk","hheub","zl","vt","bxjtjivep","p","io","xotulskjmt","mctffonh","pmeuqhoe","ghktrtq","u","ngnvwan","pqmlvvhl","enjf",
"qomcejb","twgqww","bnilyqy","nc","fttlodnz","fya","g","uoivsr","gtxgcaf","qs","gkfl","sdmacxf","mzy","xjv","yipc","rctqugjjk","myij","xxg","vyup","utqxplpsa","imbteaczlc","qfgdcz","atfn","pxcsg","f","omukbiaudb",
"uh","uobwgt","hgqipk","zunfzinenk","i","p","pet","fxai","ortqpwkukg","rxgh","ylfh"], pref = "ikwjoty"))
print(solve.prefixCount(words = ["leetcode","win","loops","success"], pref = "code"))
print(solve.prefixCount(words = ["pay","attention","practice","attend"], pref = "at"))