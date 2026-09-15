# Exercício 4

import numpy as np

latencias = [98, 102, 101, 99, 100, 103, 97, 180]

media = np.mean(latencias)
desvio = np.std(latencias)

valor = 180
z = (valor - media) / desvio

print("Média:", media)
print("Desvio-padrão:", desvio)
print("Z-Score de 180:", z)

if abs(z) > 3:
    print("Investigar: a latência merece investigação.")
else:
    print("Não ultrapassou o limite de investigação.")

print("Investigar não significa apagar automaticamente o dado.")


