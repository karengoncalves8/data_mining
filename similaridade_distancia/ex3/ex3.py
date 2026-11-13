# Exercício 3 – Distância Euclidiana com três atributos
# Atributos: [nota média, frequência (%), horas de estudo por semana]

aluno_a = [8.0, 92, 10]
aluno_b = [7.8, 90, 9]
aluno_c = [5.2, 68, 3]


def distancia_euclidiana(p, q):
    """Implementação manual: raiz da soma dos quadrados das diferenças."""
    soma = 0
    for i in range(len(p)):
        soma += (p[i] - q[i]) ** 2
    return soma ** 0.5


# 14. Distância A-B
dist_ab = distancia_euclidiana(aluno_a, aluno_b)

# 15. Distância A-C
dist_ac = distancia_euclidiana(aluno_a, aluno_c)

# 16. Exibição
print(f"Distância A-B: {dist_ab:.2f}")
print(f"Distância A-C: {dist_ac:.2f}")

# 17. Aluno mais próximo de A
if dist_ab < dist_ac:
    print("O aluno B está mais próximo de A.")
else:
    print("O aluno C está mais próximo de A.")

# Observação: a fórmula é a mesma usada com dois atributos; apenas somamos
# mais um termo (a diferença ao quadrado do terceiro atributo). A lógica
# vale para qualquer número de dimensões.
