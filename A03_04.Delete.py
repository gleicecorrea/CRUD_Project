from A01_Database import get_db_connection
from A02_Utils import (validate_date, validate_float, validate_int, sanitize_input, sanitize_input_capital,
                       validate_time)
import sys

##########################################################################
#FUNÇÕES DELETE
##########################################################################

#PRODUTO:
#########


def delete_produto(id_produto):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """DELETE FROM Produto
             WHERE IDProduto = %s"""
    cursor.execute(sql, (id_produto,))
    conn.commit()

    print(f"Produto {id_produto} eliminado com sucesso!")

    cursor.close()
    conn.close()


#VENDAS:
########

def delete_venda(id_venda):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """"DELETE FROM Venda
              WHERE IDVenda = %s"""
    cursor.execute(sql, (id_venda,))
    conn.commit()

    print(f"Venda {id_venda} anulada com sucesso!")

    cursor.close()
    conn.close()


##########################################################################
#FUNÇÕES DOS SUBMENUS:
##########################################################################

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "produto":
        #def eliminar_produto():
            id_produto = int(input("ID do Produto a eliminar: "))
            delete_produto(id_produto)

        elif sys.argv[1] == "venda":
        #def anular_venda():
            id_venda = int(input("ID da Venda a anular: "))
            delete_venda(id_venda)
        else:
            print("Argumento inválido!")
    else:
        print("Nenhum argumento transmitido.")