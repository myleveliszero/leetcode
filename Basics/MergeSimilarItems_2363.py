# Status: Bad

class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        u = []
        for i in items1:
            u.append(i[0])
        for i in items2:
            if i[0] not in u:
                u.append(i[0])
        u.sort()
        ans = []
        for i in u:
            ans.append([i,0])
        
        for idx in range(len(ans)):
            for i in items1:
                if ans[idx][0] == i[0]:
                    ans[idx][1] += i[1]
            for j in items2:
                if ans[idx][0] == j[0]:
                    ans[idx][1] += j[1]
        return ans

solve = Solution()
print(solve.mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]))