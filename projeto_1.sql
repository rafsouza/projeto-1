--
-- Arquivo gerado com SQLiteStudio v3.4.4 em sex abr 12 19:14:21 2024
--
-- Codifica�o de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabela: cliente
CREATE TABLE IF NOT EXISTS cliente (CPF NUMERIC NOT NULL, nome_cl TEXT NOT NULL, endereco TEXT NOT NULL, telefone REAL NOT NULL, email TEXT NOT NULL);

-- Tabela: compra
CREATE TABLE IF NOT EXISTS compra (produto_ID NUMERIC REFERENCES pedido (n_pedido) NOT NULL, cliente_cpf INTEGER REFERENCES cliente (CPF) NOT NULL, n_pedido INTEGER NOT NULL);

-- Tabela: itens_pedido
CREATE TABLE IF NOT EXISTS itens_pedido (n_pedido INTEGER PRIMARY KEY NOT NULL, nome TEXT NOT NULL, qtd INTEGER NOT NULL);

-- Tabela: pedido
CREATE TABLE IF NOT EXISTS pedido (n_pedido NUMERIC NOT NULL, itens TEXT NOT NULL, status TEXT NOT NULL, data_pedido TEXT NOT NULL, data_entrega TEXT NOT NULL);
INSERT INTO pedido (n_pedido, itens, status, data_pedido, data_entrega) VALUES (1, '1', 'enviado', '01-02-04', '02-02-24');
INSERT INTO pedido (n_pedido, itens, status, data_pedido, data_entrega) VALUES (2, '4', 'em seraracao', '03-03-24', '05-03-24');
INSERT INTO pedido (n_pedido, itens, status, data_pedido, data_entrega) VALUES (3, '5', 'nao enviado', '10-02-24', '12-03-24');
INSERT INTO pedido (n_pedido, itens, status, data_pedido, data_entrega) VALUES (4, '6', 'enviado ', '15-03-24', '16-03-24');
INSERT INTO pedido (n_pedido, itens, status, data_pedido, data_entrega) VALUES (5, '1', 'enviado ', '20-03-24', '22-03-24');

-- Tabela: produto
CREATE TABLE IF NOT EXISTS produto (ID NUMERIC PRIMARY KEY, nome_produto TEXT NOT NULL, qtd NUMERIC NOT NULL, porcao NUMERIC, preco NUMERIC NOT NULL, categoria TEXT NOT NULL);
INSERT INTO produto (ID, nome_produto, qtd, porcao, preco, categoria) VALUES (11117366, 'alface', 3, '', 1, 'alimento');
INSERT INTO produto (ID, nome_produto, qtd, porcao, preco, categoria) VALUES (31046749, 'couve', 5, '', 5, 'alimento');
INSERT INTO produto (ID, nome_produto, qtd, porcao, preco, categoria) VALUES (93917468, 'cenoura', 4, '', 2, 'alimento');
INSERT INTO produto (ID, nome_produto, qtd, porcao, preco, categoria) VALUES (65610830, 'salsinha', 1, '', '3,5', 'alimento');
INSERT INTO produto (ID, nome_produto, qtd, porcao, preco, categoria) VALUES (30204871, 'laranja', 2, '', 4, 'alimento ');

-- Tabela: produtor
CREATE TABLE IF NOT EXISTS produtor (CPF INTEGER NOT NULL PRIMARY KEY, nome_pr TEXT NOT NULL, endereco TEXT NOT NULL, telefone NUMERIC NOT NULL, email NUMERIC NOT NULL);
INSERT INTO produtor (CPF, nome_pr, endereco, telefone, email) VALUES (847783502, 'Ricardo', 'rua x', '(91) 2714-3785', 'ric@gmail.com');
INSERT INTO produtor (CPF, nome_pr, endereco, telefone, email) VALUES (40381633500, 'Rose', 'rua y', '(41) 2552-5815', 'rose@gmail.com');
INSERT INTO produtor (CPF, nome_pr, endereco, telefone, email) VALUES (59274408510, 'Debora', 'rua b', '(24) 3179-2635', 'debora@gmail.com');
INSERT INTO produtor (CPF, nome_pr, endereco, telefone, email) VALUES (77916369214, 'Natalia', 'rua z', '(87) 2788-6651', 'nat@gmail.com');
INSERT INTO produtor (CPF, nome_pr, endereco, telefone, email) VALUES (93467458866, 'Lais', 'avenida a', '(67) 2631-7874', 'lais@gmail.com');

-- Tabela: registra
CREATE TABLE IF NOT EXISTS registra (produtor_cpf NUMERIC REFERENCES produtor (CPF) NOT NULL, "produto_id " NUMERIC REFERENCES produto (ID) NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
