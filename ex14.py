import math

def f(x):
    return x * math.sin(x) * math.log(x)

a = float(input())
b = float(input())

n = 10**6  

h = (b - a) / n

integral = 0

for i in range(n):
    x = a + (i + 0.5) * h
    integral += f(x) * h

print(integral)
