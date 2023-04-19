class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        ans = []
        extra = []
        for i in range(len(arr2)):
            add = arr1.count(arr2[i])
            for _ in range(add):
                ans.append(arr2[i])
       
        for i in arr1:
            if i not in arr2:
                extra.append(i)
        extra.sort()

        if len(extra) != 0:
            ans.extend(extra)

        return ans

    
solve = Solution()
print(solve.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))

print(solve.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))