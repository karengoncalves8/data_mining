# Exercício 5 - Regra fixa versus Isolation Forest

from sklearn.ensemble import IsolationForest

# Consumo diário de água (litros)
consumo_agua = [
    [48], [52], [50], [55],
    [49], [53], [51], [54],
    [56], [12], [180]
]

# Regra fixa: abaixo de 30 L ou acima de 100 L é considerado incomum
LIMITE_INFERIOR = 30
LIMITE_SUPERIOR = 100

regra = [-1 if c[0] < LIMITE_INFERIOR or c[0] > LIMITE_SUPERIOR else 1 for c in consumo_agua]

modelo = IsolationForest(contamination=2 / len(consumo_agua), random_state=42)
isolation = modelo.fit_predict(consumo_agua)

print(f"Regra fixa: incomum se consumo < {LIMITE_INFERIOR} L ou > {LIMITE_SUPERIOR} L\n")
print("Dia | Consumo | Regra fixa | Isolation Forest")
for dia, (consumo, r, iso) in enumerate(zip(consumo_agua, regra, isolation), start=1):
    print(f"{dia:3} | {consumo[0]:5} L | {r:10} | {iso:16}")

candidatos_regra = [c[0] for c, r in zip(consumo_agua, regra) if r == -1]
candidatos_iso = [c[0] for c, iso in zip(consumo_agua, isolation) if iso == -1]

print("\nCandidatos pela regra fixa:", candidatos_regra)
print("Candidatos pelo Isolation Forest:", candidatos_iso)
print("Os candidatos são iguais?", "Sim" if candidatos_regra == candidatos_iso else "Não")
