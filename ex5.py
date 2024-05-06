dia = int(input())
mes = int(input())
ano = int(input())

bissexto = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

dias_por_mes = [31, 28 + bissexto, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if mes >= 1 and mes <= 12 and dia >= 1 and dia <= dias_por_mes[mes - 1]:
    print("existe")
else:
    print("não existe")
