# Status: Not Bad

class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        res = [logs[0][1]]
        idxes = [logs[0][0]]
        for i in range(len(logs)-1):
            res.append(logs[i+1][1]-logs[i][1])
            idxes.append(logs[i+1][0])
        maxval = max(res)
        ans = []
        for i in range(len(res)):
            if res[i] == maxval:
                ans.append(idxes[i])
        return min(ans)

solve = Solution()
print(solve.hardestWorker(70, [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]))    