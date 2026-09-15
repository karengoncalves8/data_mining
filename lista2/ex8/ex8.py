# Exercício 8

import pandas as pd
import numpy as np

dados = {
    "Usuario": ["ana", "bruno", "carla", "diego", "eva", "fabio"],
    "Requisicoes": [120, 135, 128, 122, 130, 400]
}

df = pd.DataFrame(dados)

media = df["Requisicoes"].mean()
desvio = df["Requisicoes"].std(ddof=0)

df["Z_Score"] = (df["Requisicoes"] - media) / desvio

def classificar(z):
    if abs(z) > 3:
        return "Investigar"
    else:
        return "Comum"

df["Status"] = df["Z_Score"].apply(classificar)

print(df[df["Status"] == "Investigar"])