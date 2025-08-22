import zipfile
from google.colab import files

# Caminho para salvar o ZIP
zip_path = '/content/Projeto-BD-Ecommerce.zip'

# Conteúdos dos arquivos
readme_content = """# Projeto Lógico de Banco de Dados – E-commerce

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
"""

criar_tabelas_sql = """-- Clientes
CREATE TABLE Cliente (
    cliente_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo CHAR(2) CHECK (tipo IN ('PF','PJ'))
);

-- Produtos
CREATE TABLE Produto (
    produto_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    fornecedor_id INT NOT NULL
);

-- Fornecedores
CREATE TABLE Fornecedor (
    fornecedor_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Estoque
CREATE TABLE Estoque (
    produto_id INT PRIMARY KEY,
    quantidade INT NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
);

-- Pedidos
CREATE TABLE Pedido (
    pedido_id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    data_pedido DATE NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);

-- Itens do Pedido
CREATE TABLE ItemPedido (
    item_id INT PRIMARY KEY,
    pedido_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES Pedido(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES Produto(produto_id)
);

-- Pagamento
CREATE TABLE Pagamento (
    pagamento_id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    tipo_pagamento VARCHAR(50) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(cliente_id)
);

-- Entrega
CREATE TABLE Entrega (
    entrega_id INT PRIMARY KEY,
    pedido_id INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    codigo_rastreio VARCHAR(50),
    FOREIGN KEY (pedido_id) REFERENCES Pedido(pedido_id)
);
"""

inserir_dados_sql = """INSERT INTO Cliente VALUES (1, 'Empresa A', 'PJ');
INSERT INTO Cliente VALUES (2, 'João Silva', 'PF');

INSERT INTO Fornecedor VALUES (1, 'Fornecedor X');
INSERT INTO Fornecedor VALUES (2, 'Fornecedor Y');

INSERT INTO Produto VALUES (1, 'Produto 1', 100.00, 1);
INSERT INTO Produto VALUES (2, 'Produto 2', 150.00, 2);

INSERT INTO Estoque VALUES (1, 50);
INSERT INTO Estoque VALUES (2, 20);

INSERT INTO Pedido VALUES (1, 2, '2025-08-22');
INSERT INTO ItemPedido VALUES (1, 1, 1, 2, 100.00);

INSERT INTO Pagamento VALUES (1, 2, 'Cartão de Crédito');

INSERT INTO Entrega VALUES (1, 1, 'Enviado', 'ABC123');
"""

queries_sql = """-- a) Recuperação simples
SELECT * FROM Cliente;

-- b) Filtros com WHERE
SELECT nome, tipo
FROM Cliente
WHERE tipo = 'PF';

-- c) Atributos derivados
SELECT produto_id, nome, preco, preco * 0.10 AS desconto
FROM Produto;

-- d) Ordenação
SELECT nome, preco
FROM Produto
ORDER BY preco DESC;

-- e) Filtros em grupos – HAVING
SELECT cliente_id, COUNT(pedido_id) AS total_pedidos
FROM Pedido
GROUP BY cliente_id
HAVING COUNT(pedido_id) > 0;

-- f) JOINs complexos
-- Produtos com fornecedores e estoque
SELECT p.nome AS produto, f.nome AS fornecedor, e.quantidade
FROM Produto p
JOIN Fornecedor f ON p.fornecedor_id = f.fornecedor_id
JOIN Estoque e ON p.produto_id = e.produto_id;

-- Pedidos com cliente e total do pedido
SELECT c.nome AS cliente, p.pedido_id, SUM(ip.quantidade * ip.preco_unitario) AS total_pedido
FROM Pedido p
JOIN Cliente c ON p.cliente_id = c.cliente_id
JOIN ItemPedido ip ON p.pedido_id = ip.pedido_id
GROUP BY c.nome, p.pedido_id;
"""

# Criar o ZIP
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.writestr('Projeto-BD-Ecommerce/README.md', readme_content)
    zipf.writestr('Projeto-BD-Ecommerce/scripts/criar_tabelas.sql', criar_tabelas_sql)
    zipf.writestr('Projeto-BD-Ecommerce/scripts/inserir_dados.sql', inserir_dados_sql)
    zipf.writestr('Projeto-BD-Ecommerce/scripts/queries.sql', queries_sql)

# Baixar o arquivo
files.download(zip_path)

