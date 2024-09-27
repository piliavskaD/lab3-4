import math

x = int(input("Enter number of x: "))
a = 7 * x + math.cos(x) + math.sqrt(x)
b1 = 3 * x - 1
b = math.pow(a, b1)
c1 = math.pow(math.e, 1.5 * x)
c = b / c1
d = math.log(abs(x), math.e)
y = c - d
print(round(y))
