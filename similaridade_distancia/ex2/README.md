# Exercício 2 – Qual cliente é mais semelhante ao cliente A?

## Resultado

| Par | Cálculo | Distância |
|---|---|---|
| A–B | √((25−27)² + (2−3)²) = √5 | **2,24** |
| A–C | √((25−45)² + (2−10)²) = √464 | 21,54 |
| A–D | √((25−52)² + (2−12)²) = √829 | 28,79 |

O cliente mais próximo de A é o **B**.

## Por que a menor distância indica maior semelhança?

A distância Euclidiana mede o quanto os valores dos atributos (idade e compras por mês) diferem entre dois clientes. Se as diferenças são pequenas, a distância é pequena.

O cliente B tem apenas 2 anos e 1 compra por mês de diferença em relação a A. Por isso tem o perfil mais parecido. Os clientes C e D são bem mais velhos e compram bem mais, então ficam distantes.

A semelhança vale **apenas para os atributos usados**. Dois clientes próximos em idade e compras podem ser bem diferentes em outros aspectos, como renda ou cidade.
