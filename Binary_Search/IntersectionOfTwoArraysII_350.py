# Status: Bad

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                ans.append(i)
        return ans

solve = Solution()
print(solve.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(solve.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))