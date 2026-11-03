# Exercício 8 - Vendas de comércio eletrônico em arquivo CSV

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import IsolationForest

pasta = Path(__file__).parent
dados = pd.read_csv(pasta.parent / "vendas_ecommerce.csv")
print(dados.head())

# id_venda e data não entram no modelo
caracteristicas = dados[["valor_total", "quantidade_itens", "desconto_percentual"]]

modelo = IsolationForest(contamination=0.15, random_state=42)
dados["rotulo"] = modelo.fit_predict(caracteristicas)
dados["valor_por_item"] = (dados["valor_total"] / dados["quantidade_itens"]).round(2)

candidatas = dados[dados["rotulo"] == -1]
print("\nVendas candidatas:")
print(candidatas.to_string())

normais = dados[dados["rotulo"] == 1]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(normais["quantidade_itens"], normais["valor_total"], c="steelblue", label="normal")
ax1.scatter(candidatas["quantidade_itens"], candidatas["valor_total"], c="red", label="candidata")
ax1.set_xlabel("Quantidade de itens")
ax1.set_ylabel("Valor total (R$)")
ax1.set_title("Valor total x quantidade de itens")

ax2.scatter(normais["desconto_percentual"], normais["valor_total"], c="steelblue", label="normal")
ax2.scatter(candidatas["desconto_percentual"], candidatas["valor_total"], c="red", label="candidata")
ax2.set_xlabel("Desconto (%)")
ax2.set_ylabel("Valor total (R$)")
ax2.set_title("Valor total x desconto")

for ax, eixo_x in ((ax1, "quantidade_itens"), (ax2, "desconto_percentual")):
    for _, linha in candidatas.iterrows():
        ax.annotate(linha["id_venda"], (linha[eixo_x], linha["valor_total"]),
                    textcoords="offset points", xytext=(5, 5))
    ax.legend()
    ax.grid(True, alpha=0.3)

fig.suptitle("Vendas do e-commerce - Isolation Forest")
fig.tight_layout()
plt.savefig(pasta / "grafico_ex8.png")
plt.show()
