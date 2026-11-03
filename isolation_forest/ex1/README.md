# Exercício 1 – Vendas de uma mercearia

## Resultado

Com `contamination=0.1`, ou seja, cerca de 1 candidato a cada 10 observações, o modelo classificou todas as vendas como normais, exceto a do **dia 10, com 400 produtos**.

## Por que uma venda muito alta pode ser uma promoção, uma encomenda ou um erro de registro?

As vendas normais ficam entre 80 e 95 produtos, e 400 é mais de quatro vezes isso. O modelo mostra que o valor é diferente, mas não diz o motivo. Pode ser uma **promoção** que atraiu muitos clientes, uma **encomenda** grande de um único comprador ou um **erro de registro**, como um zero a mais na digitação ou uma venda duplicada.

Só o contexto do negócio permite decidir entre essas hipóteses. É preciso verificar se havia promoção naquele dia, se existe nota de uma venda grande e se o estoque realmente baixou.

## Pergunta para discussão: o valor 400 deve ser removido automaticamente?

**Não.** O Isolation Forest aponta candidatos, não erros confirmados. Se a venda for real, removê-la apaga uma informação importante e distorce o faturamento.

O valor deve ser investigado primeiro e só corrigido ou removido se ficar comprovado que é um erro. Se for um evento legítimo, deve ser mantido, ou apenas marcado como "dia de promoção" para não afetar as análises do dia a dia.
