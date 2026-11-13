# Exercício 6 – Matriz de distâncias entre registros
import math

import pandas as pd

registros = {
    "A": [1, 1],
    "B": [4, 5],
    "C": [2, 2],
    "D": [5, 4],
}

nomes = list(registros)

# 28. Distância Euclidiana entre todos os pares
# 29. Matriz de distâncias em um DataFrame
matriz = pd.DataFrame(
    [[math.dist(registros[i], registros[j]) for j in nomes] for i in nomes],
    index=nomes,
    columns=nomes,
)
print("Matriz de distâncias:")
print(matriz.round(4), "\n")

# 30 e 31. Menor valor diferente de zero e par mais próximo
# Percorremos só o triângulo acima da diagonal para não repetir pares.
pares = {}
for a in range(len(nomes)):
    for b in range(a + 1, len(nomes)):
        pares[(nomes[a], nomes[b])] = matriz.iloc[a, b]

menor = min(d for d in pares.values() if d != 0)

# Pode haver empate, então guardamos todos os pares com a menor distância.
# math.isclose evita problemas de arredondamento de ponto flutuante.
mais_proximos = [p for p, d in pares.items() if math.isclose(d, menor)]

print(f"Menor distância diferente de zero: {menor:.4f}")
for x, y in mais_proximos:
    print(f"Par de registros mais próximo: {x} e {y}")
print()

# 32. A diagonal principal possui apenas zeros
# A diagonal guarda d(X, X): a distância de um registro até ele mesmo.
# Todas as diferenças entre os atributos são zero, então a soma dos
# quadrados é zero e a raiz também é zero.
diagonal_zero = all(matriz.iloc[i, i] == 0 for i in range(len(nomes)))
print(f"Diagonal principal só tem zeros? {diagonal_zero}")

# 33. A matriz é simétrica
# d(A, B) = d(B, A) porque (a - b)^2 = (b - a)^2: trocar a ordem dos
# registros só inverte o sinal de cada diferença, e o sinal desaparece ao
# elevar ao quadrado. Logo, matriz[i][j] == matriz[j][i].
simetrica = matriz.equals(matriz.T)
print(f"Matriz é simétrica? {simetrica}")
