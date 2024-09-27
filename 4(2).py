import math

def count(x1, x2, x3):
    num = abs(3.3 + math.pow(x1, 2))
    z1 = 5.126 * math.log(num, math.e)
    z2 = math.pow(x1 + math.pow(x2, 3), 1/6)
    z3 = 4 * math.tan(x3 + x1)
    z = z1 + z2 - z3
    return z
x = float(input("Enter x: "))
y = float(input("Enter y: "))
a = float(input("Enter a:"))
result = count(x, y, a)
print(result)