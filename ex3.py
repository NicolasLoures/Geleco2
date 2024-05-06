n1 = float(input())
n2 = float(input())
n3 = float(input())

media_aritmetica = (n1 + n2 + n3) / 3
media_harmonica = 3 / (1/n1 + 1/n2 + 1/n3)
media_geometrica = (n1 * n2 * n3) ** (1/3)
media_quadratica = ((n1 ** 2 + n2 ** 2 + n3 ** 2) / 3) ** 0.5

menor_media = media_aritmetica
menor_media = (media_harmonica < menor_media) and media_harmonica or menor_media
menor_media = (media_geometrica < menor_media) and media_geometrica or menor_media
menor_media = (media_quadratica < menor_media) and media_quadratica or menor_media

maior_media = media_aritmetica
maior_media = (media_harmonica > maior_media) and media_harmonica or maior_media
maior_media = (media_geometrica > maior_media) and media_geometrica or maior_media
maior_media = (media_quadratica > maior_media) and media_quadratica or maior_media

print("Menor:", menor_media)
print("Maior:", maior_media)
