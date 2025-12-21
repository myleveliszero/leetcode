from typing import List
from collections import deque
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        q = deque()
        csum, count = 0, 0
        for i in range(len(arr)):
            if i >= k:
                val = q.popleft()
                csum -= val
            q.append(arr[i])
            csum += arr[i]
            if len(q) == k:
                if csum // len(q) >= threshold:
                    count += 1
        
        return count

    def numOfSubarrays_2(self, arr: List[int], k: int, threshold: int):
        csum, count = 0, 0
        for i in range(len(arr)):
            if i >= k:
                csum -= arr[i-k]
            csum += arr[i]
            if i+1 >= k and csum // k >= threshold:
                count += 1
        return count

print(Solution().numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))
print(Solution().numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))
