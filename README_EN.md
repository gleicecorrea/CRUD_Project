# Sales Management System (CRUD with Python and MySQL)

## Objective

This project aims to build a complete product and sales management system using Python and MySQL, based on the CRUD methodology (Create, Read, Update, Delete). The system is operated through a command-line interface (CLI) and features a modular and extensible structure.

## Technologies Used

- **Programming Language:** Python 3.13
- **Database:** MySQL
- **External Libraries:** mysql-connector-python, sqlalchemy

## Object-Oriented Programming

The project applies **OOP** principles to organize business logic around domain entities such as Product, Sale, and SaleDetail. Using classes, constructors, attributes, and specific methods, it ensures:

- **Encapsulation:** each class has its own attributes and access methods.
- **Code Reusability:** `set_` and `save` methods enable reusable manipulation and persistence of objects.
- **Modular Organization:** each entity in the system represents a logical and cohesive component, facilitating maintenance and future development.

OOP makes the code more readable, separates responsibilities, and makes the system extensible for future features like advanced reporting or user authentication.

---
## Data Structure (SQL Tables)

### Product Table

```sql
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
```

### Sale Table

```sql
CREATE TABLE Venda (
IDVenda INT AUTO_INCREMENT PRIMARY KEY,
Data_Venda DATE,
Hora_Venda TIME
);
```

### SaleDetail Table

```sql
CREATE TABLE DetalheVenda(
IDVenda INT,
IDProduto INT,
PRIMARY KEY (IDVenda, IDProduto),  -- COMPOSITE PRIMARY KEY
QuantidadeVendida INT NOT NULL,
FOREIGN KEY (IDVenda) REFERENCES Venda(IDVenda),
FOREIGN KEY (IDProduto) REFERENCES Produto(IDProduto)
);
```

## Execution and Main Flow

### 1. A05_01.Main_MenuPrincipal.py

This file represents the system's entry point. It displays the **main menu** with the options:

- Product management
- Sales management

Each option redirects to a submenu via `os.system()` calls to execute Python scripts.

### 2. Submenus

- A05_02.SubMenu_GestaoProdutos.py
- A05_03.SubMenu_GestaoVendas.py

Each submenu organizes the CRUD operations for products and sales:

- Insert, list, update, and delete products
- Register sales, list sales by filters, and cancel sales

### 3. Product CRUD

#### Create - A03_01.Create.py

- The `create_produto()` function collects data and inserts it into the Product table.

#### Read - A03_02.Read.py

- `listar_produtos()` fetches all products from the database

#### Update - A03_03.Update.py

- `update_preco()` updates a product's price
- `repor_produto()` increases a product's inventory

#### Delete - A03_04.Delete.py

- `delete_produto()` removes a product from the database

### 4. Sale CRUD

#### Create - A03_01.Create.py

- `create_venda()` inserts the date/time into the Sale table
- For each item sold, a record is created in `SaleDetail`

#### Read - A03_02.Read.py

- `listar_vendas()` returns all sales
- `vendas_por_dia`, `vendas_por_produto`, and `vendas_por_mes` implement filters

#### Delete - A03_04.Delete.py

- `delete_venda()` removes a sale and its details

### 5. Database Connection

The `A01_Database.py` file contains the `get_db_connection()` function, responsible for establishing the connection with MySQL using `mysql.connector`.

### 6. Validation and Sanitization

All user inputs pass through validation functions in the `A02_Utils.py` module, such as:

- `validate_int()`
- `validate_float()`
- `validate_date()`
- `sanitize_input()`

### 7. OOP Classes

- `A04_01.Produto.py`: Product class with attributes and setters
- `A04_02.Venda.py`: Sale class with date/time
- `A04_03.DetalheVenda.py`: saves each sale's items

These classes encapsulate data and facilitate manipulation and persistence.

### 8. Database Backup - A06_BackUp_BD.py

This module performs a full backup of:

- Products
- Sales
- Sale details

The backup is done into Python lists, allowing temporary data storage for recovery in case of a system failure. It connects to the database and retrieves records using SELECT statements.

## Conclusion

This project demonstrates a real CRUD application using Python and MySQL with a modular architecture and best programming practices. Additionally, it includes extra features such as backup, input validation, and a command-line interface for retail store operations.