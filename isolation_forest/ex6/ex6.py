# Exercício 6 - Criação de um problema completo
# Contexto: acessos diários ao site de uma pequena loja virtual.
# Características: [acessos no dia, tempo médio na página (s)]

from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

acessos = [
    [520, 95], [480, 102], [550, 88], [610, 91],
    [495, 110], [530, 97], [575, 93], [505, 105],
    [590, 90], [540, 99], [560, 94], [515, 101],
    [600, 89], [3200, 4],    # dia 14: muitos acessos com permanência de poucos segundos
    [545, 96], [2100, 120],  # dia 16: muitos acessos com permanência normal
    [525, 100]
]

modelo = IsolationForest(contamination=2 / len(acessos), random_state=42)
rotulos = modelo.fit_predict(acessos)
pontuacoes = modelo.decision_function(acessos)

print("Classificação (1 = normal, -1 = candidato a anomalia):")
for dia, ((qtd, tempo), rotulo, pontuacao) in enumerate(zip(acessos, rotulos, pontuacoes), start=1):
    situacao = "candidato" if rotulo == -1 else "normal"
    print(f"Dia {dia:2}: {qtd:5} acessos, {tempo:3} s -> {rotulo:2} ({situacao}, pontuação {pontuacao:+.3f})")

candidatos = [(dia, a) for dia, (a, rotulo) in enumerate(zip(acessos, rotulos), start=1) if rotulo == -1]
print("\nCandidatos (dia, [acessos, tempo médio]):", candidatos)

cores = ["red" if rotulo == -1 else "steelblue" for rotulo in rotulos]
plt.scatter([a[0] for a in acessos], [a[1] for a in acessos], c=cores)
for dia, a in candidatos:
    plt.annotate(f"Dia {dia}", a, textcoords="offset points", xytext=(-40, 8))
plt.xlabel("Acessos no dia")
plt.ylabel("Tempo médio na página (s)")
plt.title("Acessos ao site - Isolation Forest (vermelho = candidato)")
plt.grid(True, alpha=0.3)
plt.savefig(Path(__file__).parent / "grafico_ex6.png")
plt.show()
