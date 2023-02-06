# Status: Not Bad

class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        pass

    def twopointers(self, nums1: list[int], nums2: list[int]) -> int:
        pass

    def binsearch_1(self, nums1, nums2):
        """
            len(nums1) = N
            len(nums2) = M
            Time Complexity is O(N*log(M))
            Space Complexity is O(1)
        """
        ans = 0
        for i in range(len(nums1)):
            left, right = 0, len(nums2)-1
            while left <= right:
                mid = left + (right-left)//2 
                if nums1[i] > nums2[mid]:
                    right = mid-1
                else:
                    left = mid+1
            left -= 1
            if left - i > ans:
                ans = left - i

        return ans

solve = Solution()
print(solve.binsearch_1( nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]))
print(solve.binsearch_1( nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]))