from random import randrange
from typing import *
#-2147483648
#2147483647 

def test(func1, func2, k, size, a, b):
    nums = [randrange(a, b) for _ in range(size)]
    res1 = func1(nums, k)
    res2 = func2(nums, k)
    if res1 != res2:
        print(nums)
        print(res1)
        print(res2)

# for _ in range(1000):
#     test()  

# nums1 = [1,2,2,1]
# nums2 = [9,2,2]

# counts = Counter(nums1)
# result = []

# for num in nums2:
#     print(counts[num])
#     if counts[num] > 0:
#         result.append(num)
#         counts[num] -= 1

# print(-99 % -100)

# print(-25 % -100)

# print(-25 % -3)

# print(0 % 234)
# print(0 % -234)

# -3,-2,-1 0 1 2 3

# a = [0]*2147483647
# print(a)

def test(op, input):
    obj = eval(f"{op[0]}()")
    for i in range(1, len(input)):
        if not input[i]:
            print(eval(f"obj.{op[i]}()"))
        else:
            print(eval(f"obj.{op[i]}({input[i][0]})"))

op = ["MyQueue", "push", "push", "peek", "pop", "empty"]

input = [[], [1], [2], [], [], []]

test(op, input)


