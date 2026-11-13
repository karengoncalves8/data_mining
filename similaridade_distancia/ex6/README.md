# Exercício 6 – Matriz de distâncias entre registros

## Resultado

|   | A | B | C | D |
|---|---|---|---|---|
| **A** | 0,0000 | 5,0000 | 1,4142 | 5,0000 |
| **B** | 5,0000 | 0,0000 | 3,6056 | 1,4142 |
| **C** | 1,4142 | 3,6056 | 0,0000 | 3,6056 |
| **D** | 5,0000 | 1,4142 | 3,6056 | 0,0000 |

- **Menor valor diferente de zero:** 1,4142 (√2).
- **Pares mais próximos:** há um **empate** entre **A e C** e **B e D**. Nos dois casos os registros diferem 1 unidade em cada atributo. O script lista todos os pares empatados em vez de escolher só um.
- **Diagonal principal só com zeros:** verificado (`True`).
- **Matriz simétrica:** verificado (`True`), comparando a matriz com a sua transposta.

## Por que a diagonal é zero?

A diagonal guarda a distância de cada registro até ele mesmo, d(X, X). Todas as diferenças entre os atributos são zero, então a soma dos quadrados é zero e a raiz também. Um registro é sempre idêntico a si mesmo.

## Por que d(A, B) = d(B, A)?

Trocar a ordem dos registros só inverte o sinal de cada diferença: (a − b) vira (b − a). Ao elevar ao quadrado o sinal desaparece, porque (a − b)² = (b − a)². Por isso a distância não depende da ordem e a matriz é simétrica: o valor na linha i, coluna j é igual ao valor na linha j, coluna i.

Por causa disso, basta calcular o triângulo acima da diagonal para encontrar o par mais próximo, e foi o que o script fez.
