# Status: Good

class Solution:
    def pivotInteger(self, n: int) -> int:
        numbers = [i for i in range(1, n+1)]
        answ = -1
        for i in range(n-1):
            a = sum(numbers[0:i+1])
            b = sum(numbers[i:])
            if a == b:
                answ = i+1
                break
        return answ if n != 1 else n
    def funversion(self, n):
        # Funny solution
        if n == 1:
            return 1
        elif n == 8:
            return 6
        elif n == 288:
            return 204
        elif n == 49:
            return 35
        else:
            return -1

solve = Solution()
print(solve.pivotInteger(8))
print(solve.pivotInteger(288))
print(solve.pivotInteger(999))
# temp = []
# for i in range(1, 1001):
#     temp.append(f"idx: {i}")
#     temp.append(solve.pivotInteger(i))
# print(temp)