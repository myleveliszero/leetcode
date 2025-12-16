# Status: Not Bad


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:
            j = 0
            for i in range(len(nums1)):
                if nums1[i] == 0:
                    nums1[i] = nums2[j]
                    j += 1
                    if j == n:
                        break

            nums1.sort()
    
        print(nums1)

solve = Solution()
solve.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
solve.merge(nums1=[-1,0,0,3,3,3,0,0,0], m=6, nums2=[1,2,2], n=3)