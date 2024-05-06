massa = float(input())
altura = float(input())

imc = massa / (altura ** 2)

if imc < 18.5:
    situacao = "Baixo peso"
elif 18.5 <= imc < 25:
    situacao = "Peso adequado"
elif 25 <= imc < 30:
    situacao = "Sobrepeso"
else:
    situacao = "Obesidade"

print(situacao)
