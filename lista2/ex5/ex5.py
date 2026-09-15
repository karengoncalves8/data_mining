# Exercício 5

import numpy as np

cpu = [42, 45, 47, 44, 46, 43, 48, 92]

media = np.mean(cpu)
desvio = np.std(cpu)

print("Média:", media)
print("Desvio-padrão:", desvio)

for valor in cpu:
    z = (valor - media) / desvio

    if abs(z) > 3:
        classificacao = "Investigar"
    else:
        classificacao = "Comum"

    print(valor, "->", z, "->", classificacao)
