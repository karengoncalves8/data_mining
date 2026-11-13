# Exercício 3 – Distância Euclidiana com três atributos

## Resultado

Atributos: nota média, frequência (%) e horas de estudo por semana.

| Par | Cálculo | Distância |
|---|---|---|
| A–B | √(0,2² + 2² + 1²) = √5,04 | **2,24** |
| A–C | √(2,8² + 24² + 7²) = √632,84 | 25,16 |

O aluno **B** está mais próximo de A.

## Observação: de duas para três dimensões

A lógica é a mesma do caso com dois atributos. A única mudança é somar mais um termo, a diferença ao quadrado do terceiro atributo, antes de tirar a raiz.

Por isso a função `distancia_euclidiana` usa um laço sobre os atributos. Ela funciona com 2, 3 ou qualquer número de atributos, desde que os dois registros tenham o mesmo tamanho.

Note também que a frequência (escala 0–100) domina o resultado de A–C, enquanto a nota (0–10) pesa pouco. Esse efeito de escala é o tema do exercício 5.
