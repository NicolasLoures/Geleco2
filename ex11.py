n = int(input())

primos = []

for numero in range(2, n + 1):
    eh_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            eh_primo = False
            break
    if eh_primo:
        primos.append(numero)

for primo in primos:
    print(primo)
