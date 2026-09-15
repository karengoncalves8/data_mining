# Exercício 1

media = 100
desvio = 5
valor = 115

distancia = valor - media
quantidade_desvios = distancia / desvio
z = (valor - media) / desvio

print("Distância:", distancia)
print("Quantidade de desvios-padrão:", quantidade_desvios)
print("Z-Score:", z)
print(f"O valor {valor} está {z} desvios-padrão acima da média.")
