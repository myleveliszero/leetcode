# Status: Good

# Note:
# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius*1.80 + 32.00
# Input: celsius = 10
# Ouput: [283.15, 50] == [10+273.15, 10*1.80+32.00]

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius+273.15, celsius*1.80 + 32.00] 

solve = Solution()
print(solve.convertTemperature(34.5))
print(solve.convertTemperature(21.6))

