# Exercício 2 - Latência de uma conexão de internet

from sklearn.ensemble import IsolationForest

# Tempo de resposta em milissegundos (maioria entre 20 e 70 ms, dois picos acima de 200 ms)
latencias = [
    [32], [45], [28], [51],
    [38], [62], [41], [250],
    [35], [55], [47], [30],
    [310], [44]
]

modelo = IsolationForest(contamination=2 / len(latencias), random_state=42)
rotulos = modelo.fit_predict(latencias)

print("Classificação das medições (1 = normal, -1 = candidato a anomalia):")
for i, (latencia, rotulo) in enumerate(zip(latencias, rotulos), start=1):
    situacao = "candidato" if rotulo == -1 else "normal"
    print(f"Medição {i:2}: {latencia[0]:4} ms -> {rotulo:2} ({situacao})")

candidatos = [latencia[0] for latencia, rotulo in zip(latencias, rotulos) if rotulo == -1]
print("\nCandidatos identificados (ms):", candidatos)
