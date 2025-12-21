from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.prefix = []
        for row in range(R):
            crow = [matrix[row][0]]
            for col in range(1, C):
                crow.append(matrix[row][col]+crow[-1])
            self.prefix.append(crow)
        for col in range(C):
            for row in range(1, R):
                self.prefix[row][col] += self.prefix[row-1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        big_r = self.prefix[row2][col2]
        left_r = self.prefix[row2][col1-1] if col1 > 0 else 0
        a = self.prefix[row1-1][col1-1] if (row1 > 0 and col1 > 0) else 0
        b = self.prefix[row1-1][col2] if row1 > 0 else 0
        up_r = b - a

        return big_r - left_r - up_r
    

def test(op, input):
    obj = eval(f"{op[0]}({input[0][0]})")
    for i in range(1, len(input)):
        # if not input[i]:
        #     print(eval(f"obj.{op[i]}()"))
        print(eval(f"obj.{op[i]}({input[i][0]}, {input[i][1]}, {input[i][2]}, {input[i][3]})"))
    

# inp = [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], 
#       [2, 1, 4, 3], 
#       [1, 1, 2, 2], 
#       [1, 2, 2, 4]]

# op = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]

# test(op, inp)

from random import randrange as r
def test_algo(op):
    R, C = r(100,200), r(100,200)
    matrix = [[0]*C for _ in range(R)]
    for row in range(R):
        for col in range(C):
            matrix[row][col] = r(-10, 10)

    def make_inpt():
        row1, row2 = r(0, R), r(0, R)
        while row2 < row1:
            row1, row2 = r(0, R), r(0, R)

        col1, col2 = r(0, C), r(0, C)
        while col2 < col1:
            col1, col2 = r(0, C), r(0, C)
        return [row1, col1, row2, col2]
    
    inp = [[matrix]]
    for i in range(1, len(op)):
        inp.append(make_inpt())

    print(inp)
    # for row in matrix:
    #     print(*row)
    print("Test begins")
    test(op, inp)
    print("Test ends")

op = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]

# for i in range(2):
#     test_algo(op)
    