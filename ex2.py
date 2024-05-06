a = float(input())
b = float(input())
c = float(input())

delta = b ** 2 - 4 * a * c

if delta > 0:
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)
    print("As raízes são", min(raiz1, raiz2), "e", max(raiz1, raiz2))
elif delta == 0:
    raiz = -b / (2 * a)
    print("A raiz é", raiz)
else:
    print("Nenhuma raiz")
