# Status: Not Bad

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        low, high = 0, len(arr)-1
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] - mid - 1 < k:
                low = mid+1
            else:
                high = mid-1
        return low + k


    def simple(self, arr, k):
        return [i for i in range(1, 10001) if i not in arr][k-1]

    

solve = Solution()
print(f"output: {solve.findKthPositive(arr = [2,3,4,7,11], k = 5)}", 
                f"expected: 9" )
print(f"output: {solve.findKthPositive(arr = [1,2,3,4], k = 2)}",
                f"expected: 6" )

print(f"output: {solve.simple(arr = [2,3,4,7,11], k = 5)}", 
                f"expected: 9" )
print(f"output: {solve.simple(arr = [1,2,3,4], k = 2)}",
                f"expected: 6" )