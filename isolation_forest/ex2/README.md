# Exercício 2 – Latência de uma conexão de internet

## Resultado

Foram criadas 14 medições: 12 entre 28 e 62 ms e duas acima de 200 ms. Com `contamination = 2/14`, o modelo sinalizou exatamente as medições **8 (250 ms)** e **13 (310 ms)**.

## Explicação dos candidatos

As duas medições estão muito longe do grupo de 20 a 70 ms. Por isso o Isolation Forest consegue separá-las dos outros pontos com poucos cortes. Elas representam momentos em que a conexão demorou de 4 a 6 vezes mais do que o normal para responder.

## Pergunta para discussão: uma latência alta sempre representa uma falha?

**Não.** A latência pode subir por congestionamento momentâneo na rede (downloads, atualizações), por um servidor de destino lento ou distante, por interferência no Wi-Fi ou por uma mudança de rota no provedor.

Um pico isolado costuma ser um evento pontual. Ele só passa a indicar falha quando se repete, dura muito tempo ou aparece junto com perda de pacotes.
