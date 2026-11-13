# Exercício 2 – Qual cliente é mais semelhante ao cliente A?
# Atributos: [idade, compras por mês]

cliente_a = [25, 2]
cliente_b = [27, 3]
cliente_c = [45, 10]
cliente_d = [52, 12]

# 8. Distância A-B (calculada manualmente)
dist_ab = ((cliente_a[0] - cliente_b[0]) ** 2 + (cliente_a[1] - cliente_b[1]) ** 2) ** 0.5

# 9. Distância A-C
dist_ac = ((cliente_a[0] - cliente_c[0]) ** 2 + (cliente_a[1] - cliente_c[1]) ** 2) ** 0.5

# 10. Distância A-D
dist_ad = ((cliente_a[0] - cliente_d[0]) ** 2 + (cliente_a[1] - cliente_d[1]) ** 2) ** 0.5

# 11 e 12. Comparação dos resultados para achar a menor distância
distancias = {"B": dist_ab, "C": dist_ac, "D": dist_ad}

mais_proximo = None
menor = None
for cliente, dist in distancias.items():
    if menor is None or dist < menor:
        menor = dist
        mais_proximo = cliente

# 13. Exibição
for cliente, dist in distancias.items():
    print(f"Distância A-{cliente}: {dist:.2f}")
print(f"Cliente mais próximo de A: {mais_proximo} (distância {menor:.2f})")

# Por que a menor distância indica maior semelhança?
# A distância Euclidiana mede o quanto os valores dos atributos (idade e
# compras por mês) diferem entre dois clientes. Quanto menores as diferenças
# em cada atributo, menor a distância. Assim, o cliente com a menor distância
# é aquele cuja idade e cujo volume de compras mais se parecem com os de A,
# ou seja, o que tem o perfil mais semelhante segundo esses atributos.
