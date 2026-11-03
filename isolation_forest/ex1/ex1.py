# Exercício 1 - Vendas de uma mercearia

from sklearn.ensemble import IsolationForest

vendas = [
    [80], [85], [90], [88],
    [92], [87], [95], [89],
    [91], [400]
]

modelo = IsolationForest(contamination=0.1, random_state=42)
rotulos = modelo.fit_predict(vendas)

print("Classificação das vendas (1 = normal, -1 = candidato a anomalia):")
for dia, (venda, rotulo) in enumerate(zip(vendas, rotulos), start=1):
    situacao = "candidato" if rotulo == -1 else "normal"
    print(f"Dia {dia:2}: {venda[0]:4} produtos -> {rotulo:2} ({situacao})")

sinalizados = [venda[0] for venda, rotulo in zip(vendas, rotulos) if rotulo == -1]
print("\nValor(es) sinalizado(s) pelo modelo:", sinalizados)
