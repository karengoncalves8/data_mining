# Exercício 3 - Consumo de combustível

from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# [distância (km), litros consumidos]
consumo = [
    [10, 1.0], [20, 1.8], [30, 2.6],
    [40, 3.5], [50, 4.3], [60, 5.1],
    [70, 6.0], [80, 7.0], [90, 8.0],
    [100, 20.0]
]

modelo = IsolationForest(contamination=0.1, random_state=42)
rotulos = modelo.fit_predict(consumo)

print("Classificação (1 = normal, -1 = candidato a anomalia):")
for (distancia, litros), rotulo in zip(consumo, rotulos):
    situacao = "candidato" if rotulo == -1 else "normal"
    print(f"{distancia:3} km, {litros:4} L ({distancia / litros:5.2f} km/L) -> {rotulo:2} ({situacao})")

candidatos = [linha for linha, rotulo in zip(consumo, rotulos) if rotulo == -1]
print("\nCombinação(ões) incomum(ns):", candidatos)

cores = ["red" if rotulo == -1 else "steelblue" for rotulo in rotulos]
plt.scatter([c[0] for c in consumo], [c[1] for c in consumo], c=cores)
plt.xlabel("Distância percorrida (km)")
plt.ylabel("Combustível consumido (L)")
plt.title("Consumo de combustível - Isolation Forest (vermelho = candidato)")
plt.grid(True, alpha=0.3)
plt.savefig(Path(__file__).parent / "grafico_ex3.png")
plt.show()
