# Exercício 5 – Regra fixa versus Isolation Forest

## Resultado

A regra fixa considera incomum um consumo **menor que 30 L ou maior que 100 L**. Ela e o Isolation Forest (`contamination = 2/11`) sinalizaram os mesmos valores, **12 L e 180 L**, então **os candidatos são iguais**. Isso acontece porque os dois valores estão muito longe da faixa normal, de 48 a 56 L.

## Limitações de uma regra fixa

Os limites dependem da escolha de uma pessoa. Com 10 e 200, por exemplo, a regra não encontraria nada. Eles também não se adaptam quando o padrão muda (a família cresce, chega o verão) nem servem para outros contextos, como outra casa ou um comércio.

Além disso, a regra funciona mal com várias variáveis ao mesmo tempo, porque não percebe anomalias que estão na combinação de valores, como nos exercícios 3 e 4. Ela também só diz "dentro" ou "fora", sem medir o quanto um valor é estranho.

## Por que o Isolation Forest pode ser útil quando não existe um limite definido?

O modelo aprende o padrão a partir dos próprios dados. Ele isola os pontos que se separam do grupo, sem que ninguém precise dizer qual é o consumo normal. Pode ser treinado de novo quando o padrão muda, trabalha com várias características ao mesmo tempo e dá uma pontuação que permite ordenar os casos do mais estranho para o menos estranho. A proporção esperada de anomalias (`contamination`) ainda é uma escolha de quem usa o modelo.

## Pergunta para discussão: é melhor definir manualmente um limite ou deixar o modelo aprender o padrão dos dados?

Depende do contexto. O limite manual é melhor quando existe uma referência confiável, como uma norma técnica ou um limite da concessionária, porque é simples e fácil de explicar.

O modelo é melhor quando o comportamento normal é desconhecido, muda com o tempo ou envolve várias variáveis. Na prática, o ideal é combinar os dois: usar o modelo para descobrir candidatos e transformar o que se aprendeu em regras. A decisão final sobre cada caso continua sendo humana.
