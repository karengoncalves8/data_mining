# Exercício 2

casos = [85, 100, 120]
media = 100
desvio = 10

for valor in casos:
    z = (valor - media) / desvio

    if z < 0:
        classificacao = "Abaixo da média"
    elif z > 0:
        classificacao = "Acima da média"
    else:
        classificacao = "Na média"

    print(valor, "->", z, "->", classificacao)
