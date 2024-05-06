import math

funcoes = [math.factorial, math.isqrt]

numeros = []

while True:
    entrada = input()
    if entrada == "s":
        break
    numeros.append(int(entrada))

opcao = int(input())

lista_resultante = []

if opcao == 1:
    for numero in numeros:
        lista_resultante.append(int(math.factorial(numero)))
elif opcao == 2:
    for numero in numeros:
        lista_resultante.append(int(math.isqrt(numero)))

print(lista_resultante)
