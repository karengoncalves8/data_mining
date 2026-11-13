# Exercício 4 – Comparando vários clientes com math.dist()

## Resultado

| Par | Distância |
|---|---|
| A–B | **2,24** |
| A–C | 5,83 |
| A–D | 21,54 |
| A–E | 28,79 |

> O cliente **B** possui o perfil mais próximo de A considerando idade e compras por mês.

## Observações

- `math.dist(p, q)` faz exatamente o cálculo implementado à mão nos exercícios 1 a 3. Os valores de A–B, A–D e A–E são os mesmos do exercício 2.
- O cliente mais próximo é encontrado automaticamente com `min(distancias, key=distancias.get)`, que devolve a chave com o menor valor.
