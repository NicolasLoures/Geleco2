n = int(input())
d = int(input())


multiplos = []
atual = d

# enqt o nmr atual for menor ou igual a n, add o nmr atual à lista de multiplos e incrementamos atual por d
while atual <= n:
    multiplos.append(atual)
    atual += d

print(*multiplos, sep=", ")