resultado = 0

while True:
    entrada = input()
    if entrada == "s":
        break
    numero = int(entrada)
    resultado ^= numero

print(resultado)
