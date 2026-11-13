# Exercício 5 – Influência da escala e normalização
import math

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 22. DataFrame com os dados dos clientes
df = pd.DataFrame(
    {
        "Idade": [20, 25, 40, 55, 70],
        "Renda": [2000, 3000, 6000, 9000, 12000],
    },
    index=["A", "B", "C", "D", "E"],
)
df.index.name = "Cliente"
print("Dados originais:")
print(df, "\n")

# 23. Distância A-B com os valores originais
dist_original = math.dist(df.loc["A"], df.loc["B"])
print(f"Distância A-B (valores originais): {dist_original:.4f}\n")

# 24. Normalização Min-Max (cada coluna passa para o intervalo [0, 1])
scaler = MinMaxScaler()
df_norm = pd.DataFrame(
    scaler.fit_transform(df[["Idade", "Renda"]]),
    columns=["Idade", "Renda"],
    index=df.index,
)

# 25. DataFrame normalizado
print("Dados normalizados:")
print(df_norm.round(4), "\n")

# 26. Distância A-B com os valores normalizados
dist_norm = math.dist(df_norm.loc["A"], df_norm.loc["B"])
print(f"Distância A-B (valores normalizados): {dist_norm:.4f}\n")

# 27. Comparação
dif_idade = df.loc["B", "Idade"] - df.loc["A", "Idade"]
dif_renda = df.loc["B", "Renda"] - df.loc["A", "Renda"]
print("Comparação:")
print(f"  Original: idade contribui com {dif_idade}^2 = {dif_idade ** 2}, "
      f"renda com {dif_renda}^2 = {dif_renda ** 2}")
print(f"  Original: distância = {dist_original:.4f} (praticamente a diferença de renda)")
print(f"  Normalizado: distância = {dist_norm:.4f} (as duas colunas pesam de forma equilibrada)")

# Por que a renda domina a distância com os valores originais?
# A renda varia na casa dos milhares (2.000 a 12.000), enquanto a idade varia
# na casa das dezenas (20 a 70). Como a distância Euclidiana soma as
# diferenças ao quadrado, uma diferença de 1.000 na renda (1.000.000 ao
# quadrado) esmaga uma diferença de 5 anos (25 ao quadrado). A idade
# praticamente não influencia o resultado. Após a normalização, as duas
# colunas ficam na mesma escala [0, 1] e passam a contribuir de forma
# comparável.
