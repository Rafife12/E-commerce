-- a) Recuperação simples
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
