# a = (1,2)
# b = [(1,2)]
# lst1 = [a]
# lst2 = [b]
# val1 = (lst1.pop())
# val2 = (lst2.pop())
# print(val1)
# for row, col in val1:
#     print(row,col)

# for row, col in val2:
#     print(row,col)

# print(~28)
# print(~900)
# print(~23)

# num = 999
# print(num.bit_count())
# print(num.bit_length())

# n = 0xFFFFFFFF  # 32 bits of 1
# print(f"n = {n} (0x{n:x})")
# print(f"bit_length = {n.bit_length()}")  # 32

# # Shift left - PROBLEM!
# shifted = n << 1
# print(f"n << 1 = {shifted} (0x{shifted:x})")
# print(f"bit_length after shift = {shifted.bit_length()}")  # 33, not 32!

n = 0xFFFFFFFF & 0xffffffff
print(f"n = {n} (0x{n:x})")
print(f"n = 0x{n:08x}")  # 0xffffffff

# Shift left with overflow
shifted = (n << 1) & 0xffffffff
print(f"(n << 1) & mask = 0x{shifted:08x}")  # 0xfffffffe
print(f"n << 1 = {shifted} (0x{shifted:x})")
print(f"bit_length = {shifted.bit_length()}")  # 32
# Correct: overflow bit lost, result wraps around

def test(op, input):
    obj = eval(f"{op[0]}({input[0][0]})")
    for i in range(1, len(input)):
        # if not input[i]:
        #     print(eval(f"obj.{op[i]}()"))
        print(eval(f"obj.{op[i]}({input[i][0]}, {input[i][1]}, {input[i][2]}, {input[i][3]})"))