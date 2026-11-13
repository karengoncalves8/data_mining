# Lista de Exercícios – Similaridade e Distância em Python

Cada exercício está em sua própria pasta (`ex1` a `ex6`), com o script `.py` e um `README.md` com os resultados e as respostas das perguntas abertas.

- **Parte A (ex1 a ex3):** distância Euclidiana calculada manualmente, sem `math.dist()` nem outras funções prontas.
- **Parte B (ex4 a ex6):** uso de `math.dist()`, `pandas` e `MinMaxScaler` do scikit-learn.

## Como executar

```bash
pip install pandas scikit-learn

python ex1/ex1.py
```

## Fórmula usada

Para dois registros `p` e `q` com `n` atributos:

```
d(p, q) = raiz( (p1 - q1)² + (p2 - q2)² + ... + (pn - qn)² )
```
