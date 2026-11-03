# Exercício 8 – Vendas de comércio eletrônico em arquivo CSV

## Resultado

O script lê o CSV, deixa `id_venda` e `data` fora do modelo, usa `valor_total`, `quantidade_itens` e `desconto_percentual`, aplica o Isolation Forest (`contamination=0.15`) e adiciona os rótulos ao DataFrame. As vendas candidatas foram **V011** (R$ 5.800, 1 item, 90 % de desconto), **V017** (R$ 35, 25 itens, sem desconto) e **V020** (R$ 4.200, 2 itens, 85 % de desconto). A visualização está em [grafico_ex8.png](grafico_ex8.png).

## Por que as vendas foram sinalizadas?

As vendas normais custam de R$ 72 a R$ 420, têm de 1 a 8 itens e desconto de até 20 %. **V011 e V020** têm valores mais de 10 vezes maiores, com pouquíssimos itens e desconto quase total. É uma combinação contraditória, já que um desconto alto deveria reduzir o valor da venda.

**V017** tem três vezes mais itens que a maior compra normal, por apenas R$ 1,40 cada, preço muito abaixo do praticado na loja.

## Erro, promoção legítima ou investigação?

**V011 e V020** são casos para **investigação, com forte suspeita de erro**. O valor pode ter sido registrado antes do desconto, o preço pode estar cadastrado errado ou pode ter havido fraude com cupom. Só seriam legítimas se fossem uma ação real de queima de estoque de produtos caros.

**V017** também precisa de **investigação**. Pode ser uma compra real de brindes baratos, mas também um erro de preço no cadastro ou o aproveitamento de uma falha no carrinho. Em nenhum dos casos a venda deve ser apagada sem antes conferir o pedido no sistema.
