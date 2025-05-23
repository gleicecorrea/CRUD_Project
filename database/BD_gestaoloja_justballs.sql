CREATE DATABASE gestaoloja_justballs;

CREATE TABLE Produto (
IDProduto INT AUTO_INCREMENT PRIMARY KEY,
Nome_produto VARCHAR(50),
Cor_produto VARCHAR(30),
Marca_produto VARCHAR(30),
Material_produto VARCHAR (30),
Qtd_Inventario INT NOT NULL,
Preco FLOAT NOT NULL,
taxaIVA FLOAT NOT NULL
);

CREATE TABLE Venda (
IDVenda INT AUTO_INCREMENT PRIMARY KEY,
Data_Venda DATE,
Hora_Venda TIME
);

CREATE TABLE DetalheVenda(
IDVenda INT,
IDProduto INT,
PRIMARY KEY (IDVenda, IDProduto),  -- CHAVE PRIMÁRIA COMPOSTA
QuantidadeVendida INT NOT NULL,
FOREIGN KEY (IDVenda) REFERENCES Venda(IDVenda),
FOREIGN KEY (IDProduto) REFERENCES Produto(IDProduto)
);

INSERT INTO Produto (Nome_produto, Cor_produto, Marca_produto, Material_produto, Qtd_Inventario, Preco, taxaIVA) 
VALUES ('Bola de Basquete Pro', 'Laranja', 'Spalding', 'Borrachada', 50, 299.90, 18.0),
       ('Bola de Basquete Oficial', 'Laranja', 'Wilson', 'Sintético', 100, 219.90, 18.0),
       ('Bola de Basquete Elite', 'Preto/Laranja', 'Nike', 'Couro Sintético', 30, 179.90, 18.0),
       ('Bola de Basquete Training', 'Laranja', 'Adidas', 'Borrachada', 200, 129.90, 18.0),
       ('Bola de Basquete Street', 'Laranja', 'Under Armour', 'Borrachada', 150, 109.90, 18.0),
       ('Bola de Basquete Indoor', 'Laranja', 'Molten', 'Couro', 60, 179.90, 18.0),
       ('Bola de Basquete Nova', 'Laranja', 'Nike', 'Sintético', 90, 259.90, 18.0),
       ('Bola de Basquete Pro Elite', 'Laranja', 'Spalding', 'Couro', 80, 319.90, 18.0),
       ('Bola de Basquete Junior', 'Amarela', 'Wilson', 'Borrachada', 70, 159.90, 18.0),
	   ('Bola de Basquete Treino', 'Laranja', 'Nike', 'Sintético', 120, 119.90, 18.0),
       ('Bola de Basquete Prime', 'Laranja', 'Adidas', 'Sintético', 50, 149.90, 18.0),
       ('Bola de Basquete Profi', 'Preto/Laranja', 'Molten', 'Borrachada', 40, 179.90, 18.0),
       ('Bola de Basquete Outdoor', 'Laranja', 'Under Armour', 'Sintético', 110, 139.90, 18.0),
       ('Bola de Basquete Elite Training', 'Laranja', 'Spalding', 'Couro', 90, 249.90, 18.0),
	   ('Bola de Basquete All-Star', 'Laranja', 'Wilson', 'Couro Sintético', 130, 199.90, 18.0);

SET SQL_SAFE_UPDATES=0;

UPDATE produto
SET taxaIVA = 0.23;

INSERT INTO Venda (Data_Venda, Hora_Venda) 
VALUES('2023-05-01', '10:15:00'),
	  ('2023-05-01', '11:45:00'),
	  ('2023-05-02', '14:30:00'),
      ('2023-05-02', '16:00:00'),
      ('2023-06-03', '09:00:00'),
      ('2023-06-03', '13:45:00'),
      ('2023-06-04', '12:20:00'),
      ('2023-06-04', '15:30:00'),
      ('2024-10-05', '10:05:00'),
      ('2024-10-05', '16:45:00'),
	  ('2024-10-05', '14:50:00'),
      ('2024-11-08', '18:00:00'),
      ('2024-11-07', '11:25:00'),
      ('2024-11-07', '17:40:00'),
	  ('2024-11-08', '09:10:00');


INSERT INTO DetalheVenda (IDVenda, IDProduto, QuantidadeVendida) VALUES
(1, 1, 2),
(1, 2, 1), 
(2, 3, 3),
(3, 4, 4),
(3, 5, 2),
(4, 1, 5),
(5, 6, 1),
(6, 7, 3),
(7, 8, 2),
(7, 9, 1),
(8, 10, 6),
(9, 11, 2),
(10, 12, 4),
(11, 13, 2),
(12, 14, 3);

