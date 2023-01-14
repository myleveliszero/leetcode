# Status: Not Bad

class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less, equal, greater = [], [], []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        return less + equal + greater


    

solve = Solution()
print(solve.pivotArray(nums = [9,12,5,10,14,3,10], pivot = 10))