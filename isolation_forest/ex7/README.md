# Exercício 7 – Sensores ambientais em arquivo CSV

## Resultado

O script lê o CSV com pandas, usa `temperatura` e `umidade` como características, aplica o Isolation Forest (`contamination=0.15`) e adiciona a coluna `rotulo`. As leituras candidatas foram **L011 (38 °C, 18 %)**, **L017 (8 °C, 92 %)** e **L020 (35 °C, 25 %)**. As outras ficam entre 20 e 24 °C e entre 47 e 61 % de umidade. O gráfico está em [grafico_ex7.png](grafico_ex7.png).

## Por que essas combinações de temperatura e umidade são incomuns?

As leituras normais formam um grupo fechado, em que temperatura e umidade variam pouco. L011 e L020 combinam **calor extremo com ar muito seco**, o que sugere uma fonte de calor perto do sensor ou um defeito. L017 é o oposto, **frio e quase saturado**, o que pode indicar condensação, um ar-condicionado com defeito ou uma falha de leitura.

Nos três casos, a combinação dos valores coloca o ponto muito longe da nuvem normal. Como essas leituras aparecem isoladas entre dias normais, vale verificar o sensor antes de tratá-las como reais.
