# Exercício 9

import numpy as np

dados = [10, 11, 12, 12, 13, 13, 14, 15, 30]

q1 = np.percentile(dados, 25)
q3 = np.percentile(dados, 75)

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

media = np.mean(dados)
desvio = np.std(dados)

z = (30 - media) / desvio

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Limite inferior:", limite_inferior)
print("Limite superior:", limite_superior)
print("Média:", media)
print("Desvio-padrão:", desvio)
print("Z-Score de 30:", z)

if 30 < limite_inferior or 30 > limite_superior:
    print("IQR: 30 é um possível outlier.")
else:
    print("IQR: 30 não é um possível outlier.")

if abs(z) > 3:
    print("Z-Score: 30 merece investigação.")
else:
    print("Z-Score: 30 não ultrapassa o limite de investigação.")

print("Técnicas diferentes podem analisar o mesmo dado por critérios diferentes.")
