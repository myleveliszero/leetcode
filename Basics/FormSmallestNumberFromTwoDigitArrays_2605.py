# Status: Not Bad

class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        min1 = min(nums1)
        min2 = min(nums2)

        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
        if ans != []:
            return min(ans)

        if min1 > min2:
            return int(str(min2)+str(min1))
        else:
            return int(str(min1)+str(min2))

solve = Solution()
print(solve.minNumber([6,4,3,7,2,1,8,5],[6,8,5,3,1,7,4,2]))
print(solve.minNumber([4,1,3],[5,7]))
print(solve.minNumber([3,5,2,6],[3,1,7]))   
print(solve.minNumber([5],[3]))   