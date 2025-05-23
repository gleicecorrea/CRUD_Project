from A01_Database import get_db_connection
from A02_Utils import (validate_date, validate_float, validate_int, sanitize_input, sanitize_input_capital,
                       validate_time)
import sys

##########################################################################
#FUNÇÕES UPDATE
##########################################################################

#PRODUTO:
#########


def update_preco(id_produto, novo_preco):
    if not validate_float(novo_preco):
        print("Preço deve ser um valor numérico válido.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """UPDATE Produto
             SET Preco = %s
             WHERE IDProduto = %s"""
    values = (novo_preco, id_produto)

    cursor.execute(sql, values)
    conn.commit()

    print(f"Preço do produto de ID {id_produto} atualizado com sucesso!")

    cursor.close()
    conn.close()



def repor_produto(id_produto, qtd_inventario):
    if not validate_int(qtd_inventario):
        print("Número de itens em stock deve ser um número inteiro.")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """UPDATE Produto
             SET Qtd_Inventario = Qtd_Inventario + %s
             WHERE IDProduto = %s"""
    values = (qtd_inventario, id_produto)

    cursor.execute(sql, values)
    conn.commit()

    print(f"Reposição do produto de ID {id_produto} registrada com sucesso!")
    #print("Quantidade atual do produto em estoque: {}")

    cursor.close()
    conn.close()

##########################################################################
#FUNÇÕES DOS SUBMENUS:
##########################################################################

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "produtoUp1":
        #def atualizar_preco():
            id_produto = int(input("Qual é o ID do Produto a atualizar: "))
            novo_preco = float(input("Novo preço: "))
            update_preco(id_produto, novo_preco)


        elif sys.argv[1] == "produtoUp2":
        #def registar_reposicao_produto():
            id_produto = int(input("Qual é o ID do Produto a atualizar: "))
            qtd_inventario = int(input("Quantidade a ser adicionada no estoque: "))
            repor_produto(id_produto, qtd_inventario)

        else:
            print("Argumento inválido!")
    else:
        print("Nenhum argumento transmitido.")

