# Exercício 7 - Sensores ambientais em arquivo CSV

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import IsolationForest

pasta = Path(__file__).parent
dados = pd.read_csv(pasta.parent / "sensores_ambientais.csv")
print(dados.head())

caracteristicas = dados[["temperatura", "umidade"]]

modelo = IsolationForest(contamination=0.15, random_state=42)
dados["rotulo"] = modelo.fit_predict(caracteristicas)

candidatas = dados[dados["rotulo"] == -1]
print("\nLeituras candidatas:")
print(candidatas)
print("\nIdentificadores:", candidatas["id_leitura"].tolist())

normais = dados[dados["rotulo"] == 1]
plt.scatter(normais["temperatura"], normais["umidade"], c="steelblue", label="normal")
plt.scatter(candidatas["temperatura"], candidatas["umidade"], c="red", label="candidata")
for _, linha in candidatas.iterrows():
    plt.annotate(linha["id_leitura"], (linha["temperatura"], linha["umidade"]),
                 textcoords="offset points", xytext=(5, 5))
plt.xlabel("Temperatura (°C)")
plt.ylabel("Umidade (%)")
plt.title("Sensores ambientais - Isolation Forest")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(pasta / "grafico_ex7.png")
plt.show()
