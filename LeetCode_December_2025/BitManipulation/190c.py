class Solution:
    def reverseBits(self, n: int) -> int:
        def divide_conquer(n, num_bits):
            if num_bits == 1:
                return n 
            
            half_bits = num_bits//2
            
            # n = n & ((1 << num_bits) - 1)
            mask = (1 << half_bits) - 1 
            left_bits = (n >> half_bits) & mask
            right_bits = n & mask

            left_half = divide_conquer(left_bits, half_bits)
            right_half = divide_conquer(right_bits, half_bits)


            return (right_half << half_bits) | left_half

        return divide_conquer(n, num_bits=32)
        

sol = Solution().reverseBits
print(sol(2147483644))

