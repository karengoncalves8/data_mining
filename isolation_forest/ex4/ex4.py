# Exercício 4 - Viagens de ônibus urbano

from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# [quantidade de passageiros, atraso (min)]
viagens = [
    [32, 3], [45, 5], [50, 4],
    [60, 6], [55, 5], [70, 7],
    [65, 6], [80, 8], [75, 7],
    [10, 45]
]

modelo = IsolationForest(contamination=0.1, random_state=42)
rotulos = modelo.fit_predict(viagens)

print("Classificação (1 = normal, -1 = candidato a anomalia):")
for i, ((passageiros, atraso), rotulo) in enumerate(zip(viagens, rotulos), start=1):
    situacao = "candidato" if rotulo == -1 else "normal"
    print(f"Viagem {i:2}: {passageiros:3} passageiros, {atraso:2} min de atraso -> {rotulo:2} ({situacao})")

candidatas = [viagem for viagem, rotulo in zip(viagens, rotulos) if rotulo == -1]
print("\nViagem(ns) candidata(s):", candidatas)

cores = ["red" if rotulo == -1 else "steelblue" for rotulo in rotulos]
plt.scatter([v[0] for v in viagens], [v[1] for v in viagens], c=cores)
plt.xlabel("Passageiros")
plt.ylabel("Atraso (min)")
plt.title("Viagens de ônibus - Isolation Forest (vermelho = candidato)")
plt.grid(True, alpha=0.3)
plt.savefig(Path(__file__).parent / "grafico_ex4.png")
plt.show()
