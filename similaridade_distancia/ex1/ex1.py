# Exercício 1 – Distância Euclidiana entre dois clientes
# Atributos: [idade, compras por mês]

# 1. Dados dos clientes armazenados em listas
cliente_a = [25, 2]
cliente_b = [28, 6]

# 2. Diferença entre as idades
dif_idade = cliente_a[0] - cliente_b[0]

# 3. Diferença entre as quantidades de compras
dif_compras = cliente_a[1] - cliente_b[1]

# 4. Cada diferença elevada ao quadrado
quad_idade = dif_idade ** 2
quad_compras = dif_compras ** 2

# 5. Soma dos quadrados
soma = quad_idade + quad_compras

# 6. Raiz quadrada da soma (sem funções prontas: potência 0.5)
distancia = soma ** 0.5

# 7. Resultado
print(f"Diferença de idade: {dif_idade}")
print(f"Diferença de compras: {dif_compras}")
print(f"Quadrados: {quad_idade} e {quad_compras}")
print(f"Soma dos quadrados: {soma}")
print(f"Distância Euclidiana entre A e B: {distancia:.2f}")
