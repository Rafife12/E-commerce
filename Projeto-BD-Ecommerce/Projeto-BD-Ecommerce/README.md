# Projeto Lógico de Banco de Dados – E-commerce

## Descrição do Projeto
Este projeto representa o modelo lógico de um sistema de e-commerce, contemplando clientes, produtos, pedidos, fornecedores, formas de pagamento e entregas.

## Pontos Importantes do Modelo
- Cliente pode ser PJ ou PF, mas não ambos.
- Cada cliente pode ter várias formas de pagamento.
- Entregas possuem status e código de rastreio.
- Alguns vendedores podem ser também fornecedores.
- Relacionamentos EER foram mapeados para tabelas relacionais com chaves primárias, estrangeiras e constraints de integridade.

## Estrutura de Scripts
- `criar_tabelas.sql` → Criação das tabelas com chaves primárias, estrangeiras e constraints.
- `inserir_dados.sql` → Popular o banco de dados com dados de teste.
- `queries.sql` → Consultas SQL demonstrando SELECT, WHERE, HAVING, ORDER BY, JOINs e atributos derivados.
