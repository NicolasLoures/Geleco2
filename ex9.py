print("Digite números inteiros. Digite 's' para sair.")
entrada = input()
menor_numero = int(entrada) 

while entrada != 's':
    entrada = input()
    if entrada != 's':  #
        numero = int(entrada)

        if numero < menor_numero:
            menor_numero = numero

print(menor_numero)
