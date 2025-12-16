class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        cnt = 0
        for val in stones:
            if val in jewels:
                cnt += 1
        return cnt