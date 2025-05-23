from A01_Database import get_db_connection
import sys

##########################################################################
#FUNÇÕES READ
##########################################################################

#PRODUTO:
#########

def list_all_produto():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Produto")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    if len(rows) == 0:
        print()
        print("Nenhum produto inserido!")
    cursor.close()
    conn.close()


#VENDAS:
########
import datetime


def list_all_venda():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT v.IDVenda, v.Data_Venda, v.Hora_Venda, dv.QuantidadeVendida, p.Nome_produto, p.Preco, p.taxaIVA
                     FROM venda as v
                     LEFT JOIN detalhevenda as dv 
                     ON v.IDVenda = dv.IDVenda
                     LEFT JOIN produto as p
                     ON p.IDProduto = dv.IDProduto""")
    rows = cursor.fetchall()

#Optei por fazer LEFT JOIN para mostrar todas as vendas inseridas, mesmo que elas ainda nao tenham registro de produtos (null).
#E também para poder visualizar melhor na listagem de vendas quando inserir uma nova venda, pois se fóssemos trazer somente as
#vendas concretas (que contém produtos) não as vizualizaríamos.

    for row in rows:
        id_venda, data_venda, hora_venda, quantidade_vendida, nome_produto, preco, taxa_iva = row
        data_venda_formatada = data_venda.strftime('%Y-%m-%d')   # Formata a data no formato YYYY-MM-DD
        hora_venda_formatada = str(hora_venda)                    # Converte o timedelta (hora_venda) para o formato HH:MM:SS

        print(f"IDVenda: {id_venda}, Data_Venda: {data_venda_formatada}, Hora_Venda: {hora_venda_formatada}, "
              f"Quantidade_Vendida: {quantidade_vendida}, Nome_produto: {nome_produto}, Preço: {preco}, Taxa_IVA: {taxa_iva}")

    if len(rows) == 0:
        print("Nenhuma venda inserida!")

    cursor.close()
    conn.close()


def list_vendas_dia(data_venda):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT v.IDVenda, v.Data_Venda, v.Hora_Venda, dv.QuantidadeVendida, 
                                p.Nome_produto, p.Preco, p.taxaIVA
                         FROM venda as v
                         INNER JOIN detalhevenda as dv
                         ON v.IDVenda = dv.IDVenda
                         INNER JOIN produto as p
                         ON p.IDProduto = dv.IDProduto
                         WHERE v.Data_Venda = %s""", (data_venda,))  #(data_venda,): Isso cria uma tupla de um único elemento.
    rows = cursor.fetchall()                                         #Sem a vírgula o Python tenta interpretar data_venda
                                                                     #como um valor simples, não como um único item de uma tupla.
    print(f"Vendas para o dia {data_venda}:")
    print()

    for row in rows:
        id_venda, data_venda, hora_venda, quantidade_vendida, nome_produto, preco, taxa_iva = row

        data_venda_formatada = data_venda.strftime('%Y-%m-%d')  # Formata a data no formato YYYY-MM-DD
        hora_venda_formatada = str(hora_venda)  # Converte o timedelta (hora_venda) para o formato HH:MM:SS

        print(f"IDVenda: {id_venda}, Data_Venda: {data_venda_formatada}, Hora_Venda: {hora_venda_formatada}, "
              f"Quantidade_Vendida: {quantidade_vendida}, Nome_produto: {nome_produto}, Preço: {preco}, Taxa_IVA: {taxa_iva}")

    if len(rows) == 0:
        print("Nenhuma venda inserida nessa data!")

    cursor.close()
    conn.close()


def list_vendas_produto(id_produto):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
        SELECT V.IDVenda, V.Data_Venda, V.Hora_Venda, DV.QuantidadeVendida, DV.IDProduto, P.Nome_Produto, P.Preco
        FROM Venda as V
        INNER JOIN DetalheVenda as DV ON V.IDVenda = DV.IDVenda
        INNER JOIN Produto as P ON P.IDProduto = DV.IDProduto
        WHERE DV.IDProduto = %s
    """
    cursor.execute(sql, (id_produto,))
    rows = cursor.fetchall()

    print(f"Vendas para o produto ID {id_produto}")
    print()

    for row in rows:
        id_venda, data_venda, hora_venda, quantidade_vendida, id_produto, nome_produto, preco = row

        data_venda_formatada = data_venda.strftime('%Y-%m-%d')  # Formata a data no formato YYYY-MM-DD
        hora_venda_formatada = str(hora_venda)  # Converte o timedelta (hora_venda) para o formato HH:MM:SS

        print(f"IDVenda: {id_venda}, Data_Venda: {data_venda_formatada}, Hora_Venda: {hora_venda_formatada}, "
              f"Quantidade_Vendida: {quantidade_vendida}, ID_Produto: {id_produto}, Nome_produto: {nome_produto}, Preço: {preco}")

    if len(rows) == 0:
        print("Nenhum produto vendido!")

    cursor.close()
    conn.close()


def list_vendas_mes(mes, ano):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
         SELECT V.IDVenda, V.Data_Venda, V.Hora_Venda, DV.QuantidadeVendida, DV.IDProduto, P.Nome_Produto, P.Preco
         FROM Venda as V
         INNER JOIN DetalheVenda as DV ON V.IDVenda = DV.IDVenda
         INNER JOIN Produto as P ON P.IDProduto = DV.IDProduto
         WHERE MONTH(V.Data_Venda) = %s AND YEAR(V.Data_Venda) = %s
     """
    cursor.execute(sql, (mes, ano))
    rows = cursor.fetchall()

    print(f"Vendas no mês {mes}/{ano}:")
    print()

    for row in rows:
        id_venda, data_venda, hora_venda, quantidade_vendida, id_produto, nome_produto, preco = row

        data_venda_formatada = data_venda.strftime('%Y-%m-%d')  # Formata a data no formato YYYY-MM-DD
        hora_venda_formatada = str(hora_venda)  # Converte o timedelta (hora_venda) para o formato HH:MM:SS

        print(f"IDVenda: {id_venda}, Data_Venda: {data_venda_formatada}, Hora_Venda: {hora_venda_formatada}, "
              f"Quantidade_Vendida: {quantidade_vendida}, ID_Produto: {id_produto}, Nome_produto: {nome_produto}, Preço: {preco}")

    if len(rows) == 0:
        print()
        print("Nenhuma venda referente a este mês!")
    cursor.close()
    conn.close()



##########################################################################
#FUNÇÕES DOS SUBMENUS:
##########################################################################

if __name__ == "__main__":

    if len(sys.argv) > 1:

        if sys.argv[1] == "produto":
            list_all_produto()
        elif sys.argv[1] == "venda1":
            list_all_venda()
        elif sys.argv[1] == "venda2":
            data_venda = (input("De qual data que gostaria de visualizar as vendas (AAAA-MM-DD): "))
            list_vendas_dia(data_venda)
        elif sys.argv[1] == "venda3":
            id_produto = int(input("Digite o ID do produto que gostaria de fazer a listagem: "))
            list_vendas_produto(id_produto)
        elif sys.argv[1] == "venda4":
            mes = int(input("Digite o mês (MM): "))
            ano = int(input("Digite o ano (AAAA): "))
            list_vendas_mes(mes, ano)

        else:
            print("Argumento inválido!")
    else:
        print("Nenhum argumento transmitido.")





