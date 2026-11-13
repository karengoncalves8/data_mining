# Exercício 4 – Comparando vários clientes com math.dist()
# Atributos: [idade, compras por mês]

# 18. Importação do módulo math
import math

clientes = {
    "A": [25, 2],
    "B": [27, 3],
    "C": [30, 5],
    "D": [45, 10],
    "E": [52, 12],
}

referencia = clientes["A"]

# 19 e 20. Distância de A para os demais clientes
distancias = {}
for nome, valores in clientes.items():
    if nome == "A":
        continue
    distancias[nome] = math.dist(referencia, valores)
    print(f"Distância A-{nome}: {distancias[nome]:.2f}")

# 21. Cliente mais próximo identificado automaticamente
mais_proximo = min(distancias, key=distancias.get)

print(
    f"\nO cliente {mais_proximo} possui o perfil mais próximo de A considerando "
    f"idade e compras por mês (distância {distancias[mais_proximo]:.2f})."
)
