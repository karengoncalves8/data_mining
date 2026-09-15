# Exercício 10

import pandas as pd
import numpy as np

dados = {
    "Evento": ["A", "B", "C", "D", "E", "F", "G"],
    "Tentativas_Login": [3, 4, 2, 5, 3, 4, 40]
}

df = pd.DataFrame(dados)

media = df["Tentativas_Login"].mean()
desvio = df["Tentativas_Login"].std(ddof=0)

df["Z_Score"] = (
    df["Tentativas_Login"] - media
) / desvio

df["Status"] = np.where(
    df["Z_Score"].abs() > 3,
    "Investigar",
    "Comum"
)

print(df)

print("\nEventos para investigar:")
print(df[df["Status"] == "Investigar"])

print(
    "\nUm evento incomum em segurança pode ser justamente "
    "o dado mais importante da análise."
)