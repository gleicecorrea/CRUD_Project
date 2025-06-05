
# Just Balls - Sistema de Gestão de Produtos e Vendas

## 📌 Objetivo
Este projeto tem como objetivo desenvolver um sistema de gestão para uma loja de artigos desportivos chamada **Just Balls**, utilizando **Python** e **MySQL** para realizar operações de **CRUD** (Create, Read, Update, Delete), além de possuir funcionalidades analíticas e de backup.

---

## ⚙️ Descrição Geral do Projeto

O sistema é um aplicativo de terminal organizado em menus e submenus. Ele interage com um banco de dados MySQL para gerir produtos, registrar vendas e manter dados consistentes.

### 🛠️ Tecnologias Utilizadas

- Python 3.x
- MySQL
- SQLAlchemy (em partes do projeto)
- Sistema de menus via terminal
- Estrutura modularizada em arquivos Python

---

## 🗃️ Estrutura do Banco de Dados

O banco de dados possui as seguintes tabelas principais:

### `Produto`

| Campo             | Tipo         | Descrição                        |
|------------------|--------------|----------------------------------|
| IDProduto        | INT (PK)     | Identificador do produto         |
| Nome_produto     | VARCHAR      | Nome do produto                  |
| Cor_produto      | VARCHAR      | Cor do produto                   |
| Marca_produto    | VARCHAR      | Marca                            |
| Material_produto | VARCHAR      | Tipo de material                 |
| Qtd_inventario   | INT          | Quantidade disponível em estoque|
| Preco            | FLOAT        | Preço unitário                   |
| taxaIVA          | FLOAT        | Taxa de IVA aplicada (%)         |

### `Venda`

| Campo       | Tipo     | Descrição               |
|------------|----------|-------------------------|
| IDVenda    | INT (PK) | Identificador da venda  |
| Data_Venda | DATE     | Data da venda           |
| Hora_Venda | TIME     | Hora da venda           |

### `DetalheVenda`

| Campo             | Tipo     | Descrição                              |
|------------------|----------|------------------------------------------|
| IDVenda          | INT (FK) | Venda relacionada                        |
| IDProduto        | INT (FK) | Produto relacionado                      |
| QuantidadeVendida| INT      | Quantidade de produto vendido            |

---

## 🧩 Organização do Projeto

O projeto está dividido em módulos, cada um com responsabilidade específica:

### 🔹 `A01_Database.py`

- Faz a conexão com o banco de dados MySQL.

### 🔹 `A02_Utils.py`

- Contém funções auxiliares como validações de tipos, sanitização de inputs, validação de data e hora.

### 🔹 `A03_01.Create.py`

- **Função Produto:** Inserção de um novo produto no sistema.
- **Função Venda:** Registra uma nova venda e seus detalhes.

### 🔹 `A03_02.Read.py`

- Listagem de produtos e vendas.
- Filtros por dia, produto e mês.

### 🔹 `A03_03.Update.py`

- Atualiza o preço do produto.
- Reposição de estoque.

### 🔹 `A03_04.Delete.py`

- Remove produtos e vendas do banco de dados.

### 🔹 `A04_01.Produto.py`

- Define a classe `Produto` com atributos e métodos de atualização.

### 🔹 `A04_02.Venda.py`

- Define a classe `Venda` com setters para data e hora.

### 🔹 `A04_03.DetalheVenda.py`

- Classe `DetalheVenda` para registrar itens vendidos por venda.
- Métodos para listar e consultar por produto.

### 🔹 `A05_01.Main_MenuPrincipal.py`

- Menu principal do sistema, com acesso aos submenus de produtos e vendas.

### 🔹 `A05_02.SubMenu_GestaoProdutos.py`

- Submenu CRUD completo de produtos.

### 🔹 `A05_03.SubMenu_GestaoVendas.py`

- Submenu completo de operações sobre vendas.

### 🔹 `A06_BackUp_BD.py`

- Realiza backup local (em memória) de todas as tabelas principais (`Produto`, `Venda`, `DetalheVenda`).

---

## 💾 Sistema de Backup

O script `A06_BackUp_BD.py` realiza cópias em listas locais dos dados contidos nas tabelas, permitindo restauração ou análises futuras mesmo com perda temporária de conexão.

```python
# Exemplo simplificado:
cursor.execute("SELECT * FROM Produto")
produtos_local.append(Produto(...))
```

Esse processo é útil para manter integridade temporária dos dados ou preparar snapshots antes de alterações.

---

## ▶️ Execução

1. Garanta que o MySQL está rodando e o banco está criado.
2. Rode o menu principal com:

```bash
python A05_01.Main_MenuPrincipal.py
```

3. Navegue pelas opções com os menus intuitivos.

---

## 📚 Conceitos Aplicados

- **CRUD** com SQL integrado via Python.
- **Orientação a Objetos** (classes `Produto`, `Venda`, `DetalheVenda`).
- Separação de responsabilidades por módulo.
- Backup e persistência de dados.
- Operações SQL seguras com uso de placeholders.

---

## ✨ Contribuições Futuras

- Interface gráfica com Tkinter ou PyQt.
- Backup em arquivos `.json` ou `.csv`.
- Testes unitários e validação contínua.
- Relatórios analíticos de vendas.

---

**Desenvolvido para fins educacionais e prática de integração Python + MySQL.**
