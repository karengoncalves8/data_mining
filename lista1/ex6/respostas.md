Fiz com o postgresSQL pois já tem integração direta com o Orange


### a) Quais problemas foram encontrados?

Foram identificados dados vazios, valores inválidos, registros duplicados e inconsistências entre informações relacionadas.

Entre os dados vazios foram encontrados telefone, e-mail e cidade sem preenchimento. Entre os valores inválidos foram identificados um endereço de e-mail em formato incorreto, preço negativo de produto, quantidades iguais ou inferiores a zero, desconto superior a 100% e uma data de venda futura.

Também foram encontradas duplicidades de CPF de cliente, de cadastro de produto e de uma venda. Por fim, foram identificadas inconsistências como valor total diferente do resultado esperado da venda, preço da venda diferente do preço cadastrado para o produto, combinação incorreta entre cidade e estado e uma venda marcada como cancelada que ainda possuía valor positivo.


### b) Em quais campos eles apareceram?

Os problemas apareceram nos seguintes campos:

* Dados vazios: `telefone`, `email` e `cidade`;
* Valores inválidos: `email`, `preco`, `quantidade`, `desconto_percentual` e `data_venda`;
* Duplicidades: `cpf` do cliente, dados do produto e conjunto de informações que caracteriza uma venda;
* Inconsistências: `valor_total`, `preco_unitario`, `preco` do catálogo, `cidade`, `estado` e `status`.

A análise mostrou também que alguns erros podem afetar mais de um campo. Por exemplo, uma quantidade inválida pode fazer com que o valor total armazenado não corresponda ao valor que deveria ser calculado.


### c) Quantos registros foram afetados?

Foram introduzidos diretamente:

* 3 registros com dados vazios;
* 6 registros com valores inválidos;
* 3 duplicatas lógicas, correspondentes a três pares de registros duplicados;
* 4 registros com inconsistências intencionais.

No caso das duplicidades, se forem contabilizados todos os registros pertencentes aos três pares, existem 6 registros envolvidos. Se forem contabilizadas somente as cópias excedentes, existem 3 duplicatas.

Além disso, durante as verificações foi possível observar problemas derivados. Algumas alterações, como quantidade, desconto ou preço incorreto, também provocaram divergências nos cálculos das vendas. Isso demonstra que um mesmo registro pode participar de mais de uma categoria de problema, portanto não é correto simplesmente somar todas as categorias para obter um número único de registros distintos.


### d) O fato de os dados estarem armazenados em um banco de dados garante que eles estejam corretos? Explique.

Não. O fato de os dados estarem armazenados em um banco de dados não garante que estejam corretos.

O PostgreSQL garante que os dados sejam armazenados seguindo as regras definidas no esquema do banco, mas ele não consegue determinar automaticamente todas as regras do negócio. Por exemplo, se a tabela permitir qualquer valor numérico para a quantidade, o banco poderá armazenar `-2`, mesmo que uma quantidade negativa não faça sentido para uma venda.

Da mesma maneira, um campo de texto pode armazenar um e-mail como `email-invalido` se não existir uma regra que valide seu formato. O banco também pode permitir clientes com o mesmo CPF caso não exista uma restrição de unicidade.

Portanto, a qualidade dos dados depende da definição de regras de integridade, validações, restrições como `NOT NULL`, `UNIQUE`, `CHECK` e chaves estrangeiras, além de validações realizadas pela própria aplicação.

A análise no Orange mostrou justamente que dados podem estar tecnicamente armazenados de maneira válida no PostgreSQL e, ao mesmo tempo, estar incorretos ou inconsistentes do ponto de vista do negócio. Por isso, armazenamento, integridade estrutural e qualidade dos dados são conceitos relacionados, mas diferentes.
