import mysql.connector


class Produto:
    def __init__(self, nome, cor, marca, material, qtd_inventario, preco, taxa_iva):
        self.nome = nome
        self.cor = cor
        self.marca = marca
        self.material = material
        self.qtd_inventario = qtd_inventario
        self.preco = preco
        self.taxa_iva = taxa_iva


    def set_nome(self, nome):
        self.nome = nome

    def set_cor(self, cor):
        self.cor = cor

    def set_marca(self, marca):
        self.marca = marca

    def set_material(self, material):
        self.material = material

    def set_qtd_inventario(self, qtd_inventario):
        self.qtd_inventario = qtd_inventario

    def set_preco(self, preco):
        self.preco = preco

    def set_taxa_iva(self, taxa_iva):
        self.taxa_iva = taxa_iva










#class Produto: Aqui estamos criando uma classe chamada Produto. Uma classe é uma estrutura que permite
# agrupar dados e funções (métodos) que operam sobre esses dados. O Produto representará um item no
# nosso inventário, com atributos como nome, cor, preço, etc.

#3. O Metodo Construtor __init__ :

#__init__(self, ...): Esse é o metodo construtor da classe Produto. Ele é chamado automaticamente
# quando um objeto da classe Produto é criado.

#self: O self refere-se ao objeto atual da classe. Ele é utilizado para acessar os atributos e métodos dentro
# da própria classe.

#Atributos: Este metodo define os atributos que um objeto Produto terá (como nome, cor, marca, etc.) e os
# inicializa com os valores passados ao criar o objeto.

#############################################################################################################

#4. Métodos Setters (Definindo Atributos)
#Esses métodos permitem atualizar os atributos do objeto Produto depois que ele já foi criado.

#set_nome(self, nome): Este é um setter para o atributo nome. Ele permite que você altere o nome do produto
# após o objeto ser criado.

#Os outros métodos set_*: O mesmo raciocínio se aplica aos outros métodos setters (para cor, marca, material,
# etc.). Eles permitem que você altere os atributos do produto individualmente após a criação do objeto.

############################################################################################################

#5. Metodo save (Inserir Produto no Banco de Dados)

#save(self, cursor): Este metodo insere o produto atual no banco de dados. Ele recebe um cursor como
#argumento, que é a ferramenta usada para executar comandos SQL no banco de dados.

#cursor.execute(...): O metodo execute executa a consulta SQL que inserirá os dados do produto no banco
# de dados. O SQL usado aqui é um INSERT INTO, que adiciona um novo registro na tabela Produto.

#     *Parâmetros (%s, %s, ...): Esses são placeholders (marcadores de posição) que serão substituídos pelos
#       valores reais dos atributos do produto (self.nome, self.cor, etc.) no momento da execução da consulta.

#     *(self.nome, self.cor, ...): Esses são os valores que vão substituir os placeholders no comando SQL.

############################################################################################################

#6. Metodo list_all (Listar Todos os Produtos)

#@staticmethod: Este é um decorador que indica que o metodo list_all é um metodo estático. Isso
# significa que ele pode ser chamado sem a necessidade de criar um objeto da classe Produto.
# O metodo estático não acessa nem modifica os atributos da instância da classe (não usa self).

#cursor.execute("SELECT * FROM Produto"): Executa a consulta SQL SELECT, que retorna todos os registros da
# tabela Produto.

#cursor.fetchall(): Retorna todos os resultados da consulta como uma lista de tuplas. Cada tupla representa
# uma linha da tabela Produto.