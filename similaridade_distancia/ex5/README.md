# Exercício 5 – Influência da escala e normalização

## Resultado

| Situação | Distância A–B |
|---|---|
| Valores originais | **1000,0125** |
| Valores normalizados (MinMaxScaler) | **0,1414** |

Valores normalizados (cada coluna vai para o intervalo [0, 1] com `(x − mín) / (máx − mín)`):

| Cliente | Idade | Renda |
|---|---|---|
| A | 0,0 | 0,0 |
| B | 0,1 | 0,1 |
| C | 0,4 | 0,4 |
| D | 0,7 | 0,7 |
| E | 1,0 | 1,0 |

## Comparação

Com os valores originais, a distância (1000,0125) é praticamente igual à diferença de renda (1000). A diferença de 5 anos de idade quase não muda nada: só acrescenta 0,0125.

Depois da normalização, A e B diferem 0,1 em cada coluna. As duas colunas passam a contribuir igualmente e a distância fica √(0,1² + 0,1²) ≈ 0,1414.

## Por que a renda tem influência muito maior com os valores originais?

A distância Euclidiana soma as **diferenças ao quadrado** de cada atributo, sem levar em conta a unidade de cada um.

- A renda varia na casa dos **milhares** (R$ 2.000 a R$ 12.000). A diferença entre A e B é 1.000, que ao quadrado vira **1.000.000**.
- A idade varia na casa das **dezenas** (20 a 70). A diferença entre A e B é 5, que ao quadrado vira apenas **25**.

A renda responde por mais de 99,99% da soma, então a idade é praticamente ignorada. Isso não acontece porque a renda seja mais importante para o problema, mas só porque os números dela são maiores.

A normalização coloca todos os atributos na mesma escala. Assim, cada um contribui de forma comparável para a distância. Por isso é recomendável normalizar os dados antes de usar métodos baseados em distância, como KNN e K-Means.

Neste conjunto de dados, idade e renda crescem na mesma proporção. Por isso as duas colunas normalizadas ficaram idênticas.
