########################################################
# Passo 01: Configurar a Base de Dados MySQL
########################################################

# 01. certifique-se de que tem um servidor MySQL
#      a correr e crie a base de dados e as tabelas:

'''

CRIAÇÃO DA BASE DE DADOS:

DROP DATABASE IF EXISTS gestaoloja_justballs;
CREATE DATABASE IF NOT EXISTS gestaoloja_justballs;
USE gestaoloja_justballs;


CRIAÇÃO DAS TABELAS:

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

'''


########################################################
# Passo 02: Instalar Pacotes Necessários
########################################################

#pip install mysql-connector-python

########################################################
# Passo 03: Conexão com a Base de Dados (database.py)
########################################################

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="123456",
        database="gestaoloja_justballs",
        use_pure=True)