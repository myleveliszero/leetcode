# Status: Bad
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        pass
    def bruforce(self, arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == 2*arr[j] or 2*arr[i] == arr[j]:
                    return True
        return False

solve = Solution()
print(solve.checkIfExist(arr = [3,1,7,11]))
print(solve.checkIfExist(arr = [10,2,5,3]))
print(solve.checkIfExist(arr = [7,1,14,11]))

