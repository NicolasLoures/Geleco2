a = int(input())
b = int(input())

for numero in range(a, b + 1):
    if numero % 3 == 0 and numero % 5 == 0 and numero % 7 != 0:
        print(numero)
