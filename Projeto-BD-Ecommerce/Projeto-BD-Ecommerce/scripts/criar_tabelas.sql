-- Clientes
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
