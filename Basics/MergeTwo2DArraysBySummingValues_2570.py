# Status: Not Bad

from collections import defaultdict
from itertools import zip_longest

class Solution:
    def mergeArrays(self, nums1, nums2):
        dic = defaultdict(int)
        for i, j in zip_longest(nums1, nums2, fillvalue=[0,0]):
            if i[0] <= j[0]:
                dic[i[0]] += i[1]
                dic[j[0]] += j[1]
            else:
                dic[j[0]] += j[1]
                dic[i[0]] += i[1]
        ans = []
        for i in dic:
            if i != 0:
                ans.append([i,dic[i]])
        
        return sorted(ans)
        

solve = Solution()
print(solve.mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]))
print(solve.mergeArrays(nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]))