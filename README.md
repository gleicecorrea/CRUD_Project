# Just Balls - Sistema de Gestão de Vendas (CRUD com Python e MySQL)

## Objetivo

Este projeto tem como finalidade a construção de um sistema completo de gestão de produtos e vendas utilizando Python e MySQL, com base na metodologia CRUD (Create, Read, Update, Delete). O sistema é operado por linha de comando (CLI) e possui uma estrutura modular e extensível.

## Tecnologias Utilizadas

- **Linguagem de Programação:** Python 3.x
- **Banco de Dados:** MySQL
- **Bibliotecas externas:** mysql-connector-python, sqlalchemy (pontualmente usada)
- **Sistema Operacional:** Compatível com Windows/Linux

## Estrutura de Dados (Tabelas SQL)

### Tabela Produto

```sql
CREATE TABLE Produto (
    IDProduto INT AUTO_INCREMENT PRIMARY KEY,
    Nome_produto VARCHAR(100),
    Cor_produto VARCHAR(50),
    Marca_produto VARCHAR(50),
    Material_produto VARCHAR(50),
    Qtd_inventario INT,
    Preco DECIMAL(10, 2),
    taxaIVA FLOAT
);
```

### Tabela Venda

```sql
CREATE TABLE Venda (
    IDVenda INT AUTO_INCREMENT PRIMARY KEY,
    Data_Venda DATE,
    Hora_Venda TIME
);
```

### Tabela DetalheVenda

```sql
CREATE TABLE DetalheVenda (
    IDDetalheVenda INT AUTO_INCREMENT PRIMARY KEY,
    IDVenda INT,
    IDProduto INT,
    QuantidadeVendida INT,
    FOREIGN KEY (IDVenda) REFERENCES Venda(IDVenda),
    FOREIGN KEY (IDProduto) REFERENCES Produto(IDProduto)
);
```

## Execução e Fluxo Principal

### 1. `A05_01.Main_MenuPrincipal.py`

Este arquivo representa o ponto de entrada do sistema. Ele exibe o **menu principal** com as opções de:

- Gestão de produtos
- Gestão de vendas

Cada opção redireciona para um submenu através de chamadas `os.system()` para execução de scripts Python.

### 2. Submenus

- `A05_02.SubMenu_GestaoProdutos.py`
- `A05_03.SubMenu_GestaoVendas.py`

Cada submenu organiza as operações de CRUD com produtos e vendas:

- Inserir, listar, atualizar e deletar produtos
- Registrar vendas, listar vendas por filtro e anular

### 3. CRUD de Produto

#### Create - `A03_01.Create.py`

- Função `create_produto()` coleta os dados e insere na tabela Produto.

#### Read - `A03_02.Read.py`

- `listar_produtos()` busca todos os produtos da base

#### Update - `A03_03.Update.py`

- `update_preco()` atualiza o preço de um produto
- `repor_produto()` incrementa o estoque de um produto

#### Delete - `A03_04.Delete.py`

- `delete_produto()` remove um produto da base

### 4. CRUD de Venda

#### Create - `A03_01.Create.py`

- `create_venda()` insere a data/hora na tabela Venda
- Para cada item vendido, é criado um registro em `DetalheVenda`

#### Read - `A03_02.Read.py`

- `listar_vendas()` traz todas as vendas
- `vendas_por_dia`, `vendas_por_produto`, `vendas_por_mes` implementam filtros

#### Delete - `A03_04.Delete.py`

- `delete_venda()` remove a venda e seus detalhes

### 5. Conexão com o Banco de Dados

O arquivo `A01_Database.py` possui a função `get_db_connection()`, responsável por estabelecer a conexão com o MySQL utilizando `mysql.connector`.

### 6. Validações e Sanitização

Todas as entradas do usuário passam por funções de validação no módulo `A02_Utils.py`, como:

- `validate_int()`
- `validate_float()`
- `validate_date()`
- `sanitize_input()`

### 7. Classes POO

- `A04_01.Produto.py`: classe Produto com atributos e setters
- `A04_02.Venda.py`: classe Venda com data/hora
- `A04_03.DetalheVenda.py`: salva os itens de cada venda

Essas classes encapsulam os dados e facilitam a manipulação e persistência.

### 8. Backup do Banco de Dados - `A06_BackUp_BD.py`

Este módulo realiza o backup completo de:

- Produtos
- Vendas
- Detalhes das vendas

O backup é feito em listas Python, o que permite salvar os dados temporariamente para recuperação em caso de falha no sistema. O backup é feito conectando ao banco e extraindo os registros com SELECTs.

## Conclusão

Este projeto demonstra uma aplicação CRUD real utilizando Python e MySQL com arquitetura modular, boas práticas de programação e separação de responsabilidades. Além disso, inclui recursos adicionais como backup, validações de entrada e interface via linha de comando para operações comerciais de uma loja de varejo.

O projeto é ideal para demonstrar competências em backend Python, modelagem de dados e integração com bancos relacionais.