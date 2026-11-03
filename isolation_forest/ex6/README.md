# Exercício 6 – Criação de um problema completo

## Contexto e resultado

O contexto escolhido foram os **acessos diários ao site de uma loja virtual**, com 17 observações de dois tipos: quantidade de acessos e tempo médio na página. Em um dia normal, o site tem de 480 a 610 acessos, e cada visitante fica de 88 a 110 s. Foram incluídas duas situações incomuns: o **dia 14** (3200 acessos, 4 s) e o **dia 16** (2100 acessos, 120 s).

Com `contamination = 2/17`, o Isolation Forest sinalizou exatamente os dias 14 e 16, que tiveram as únicas pontuações negativas. O gráfico está em [grafico_ex6.png](grafico_ex6.png).

## Avaliação de cada candidato

O **dia 14** é um **caso para investigação, com suspeita de tráfego não humano**. Um volume 6 vezes maior que o normal, com visitantes que saem quase na hora, é típico de robôs ou ataques. Esse tráfego não gera vendas e distorce as métricas, por isso deve ser verificado nos logs do servidor.

O **dia 16** parece um **evento legítimo**. Muitos acessos com visitas longas indicam pessoas reais e interessadas, provavelmente por causa de uma campanha ou promoção. Vale confirmar com a equipe de marketing, mas o dado não deve ser descartado.

## Pergunta para discussão: quais critérios foram usados para decidir que uma observação era incomum?

O primeiro critério foi a **distância em relação ao grupo** de dias normais, que é bem concentrado. O segundo foi a **combinação das características**: muitos acessos com tempo quase zero não combinam com o comportamento de visitantes reais.

O terceiro foi a **pontuação do modelo**: os pontos isolados com menos cortes ficaram com pontuação negativa. Por fim, o **conhecimento do negócio** foi necessário para classificar cada candidato como erro, evento legítimo ou caso para investigação.
