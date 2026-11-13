# Exercício 1 – Distância Euclidiana entre dois clientes

## Resultado

| Passo | Cálculo | Valor |
|---|---|---|
| Diferença de idade | 25 − 28 | −3 |
| Diferença de compras | 2 − 6 | −4 |
| Quadrados | (−3)², (−4)² | 9 e 16 |
| Soma | 9 + 16 | 25 |
| Raiz | √25 | **5,00** |

A distância Euclidiana entre os clientes A e B é **5,00**.

## Observações

- A raiz quadrada foi calculada com `soma ** 0.5`, sem `math.dist()` nem `math.sqrt()`, como pede a restrição.
- O sinal negativo das diferenças não importa, porque some quando elevamos ao quadrado.
