from A01_Database import get_db_connection
from A02_Utils import (validate_date, validate_float, validate_int, sanitize_input, sanitize_input_capital,
                       validate_time)
import sys

##########################################################################
#FUNÇÕES CREATE
##########################################################################

#PRODUTO:
#########

#INICIAL:
#def create_produto(nome, cor, marca, material, qtd_inventario, preco, taxa_iva):
#    if not validate_int(qtd_inventario):
#        print("Número de itens em stock deve ser um número inteiro.")
#        return
#    if not validate_float(preco) or not validate_float(taxa_iva):
#        print("Preço e taxa de IVA devem ser valores numéricos válidos.")
#        return
#
#    conn = get_db_connection()   -> estabelece a conexao com a base de dados
#    cursor = conn.cursor()       -> cria o cursor
#
#    sql = """INSERT INTO Produto (Nome_produto, Cor_produto, Marca_produto, Material_produto, Qtd_Inventario, Preco, taxaIVA)
#           VALUES (%s, %s, %s, %s, %s, %s, %s)"""
#    values = (sanitize_input_capital(nome), sanitize_input(cor), sanitize_input_capital(marca), sanitize_input(material), qtd_inventario, preco, taxa_iva)
#
#    cursor.execute(sql, values)     -> Executa
#    conn.commit()                   -> Salva as alterações na Base de Dados
#
#    print(f"Produto '{nome}' criado com sucesso!")
#
#    cursor.close()                -> fecho manual da conexao e cursor
#    conn.close()

#COM MELHORIAS:
def create_produto(nome, cor, marca, material, qtd_inventario, preco, taxa_iva):
    if not validate_int(qtd_inventario):
        print("Número de itens em stock deve ser um número inteiro.")
        return
    if not validate_float(preco) or not validate_float(taxa_iva):
        print("Preço e taxa de IVA devem ser valores numéricos válidos.")
        return

    try:                                      #try except introduzido para capturar e tratar qlq erro
        with get_db_connection() as conn:    #Uso de with garante que a conexao e o cursor serão fechados, seja por sucesso ou erro
            with conn.cursor() as cursor:
                sql = """INSERT INTO Produto (Nome_produto, Cor_produto, Marca_produto, Material_produto, 
                          Qtd_Inventario, Preco, taxaIVA)
                         VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                values = (sanitize_input_capital(nome), sanitize_input(cor), sanitize_input_capital(marca),
                          sanitize_input(material), qtd_inventario, preco, taxa_iva)
                cursor.execute(sql, values)
                conn.commit()

                print(f"Produto '{nome}' criado com sucesso!")

    except Exception as e:
        print(f"Erro ao criar produto: {e}")



#VENDAS:
########

#INICIAL:
#def create_venda(data_venda, hora_venda):
#    if not validate_date(data_venda):
#        print("A data precisa estar no formato 'YYYY-MM-DD'.")
#        return
#    if not validate_time(hora_venda):
#        print("A hora precisa estar no formato 'HH:MM:SS'.")
#        return
#
#    conn = get_db_connection()
#    cursor = conn.cursor()
#
#    sql = """INSERT INTO Venda (Data_Venda, Hora_Venda)
#            VALUES (%s, %s)"""
#    values = (data_venda, hora_venda)
#
#    cursor.execute(sql, values)
#    conn.commit()
#
#    print(f"Venda registrada com sucesso!")
#
#    cursor.close()
#    conn.close()

#COM MELHORIAS:
def create_venda(data_venda, hora_venda):
    if not validate_date(data_venda):
        print("A data precisa estar no formato 'YYYY-MM-DD'.")
        return
    if not validate_time(hora_venda):
        print("A hora precisa estar no formato 'HH:MM:SS'.")
        return

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                sql = """INSERT INTO Venda (Data_Venda, Hora_Venda)
                         VALUES (%s, %s)"""
                values = (data_venda, hora_venda)
                cursor.execute(sql, values)
                conn.commit()

                print(f"Venda registrada com sucesso!")

    except Exception as e:
        print(f"Erro ao registrar venda: {e}")



##########################################################################
#FUNÇÕES DOS SUBMENUS:
##########################################################################
if __name__ == "__main__":

    if len(sys.argv) > 1:   #Verifica se existe algum argumento que foi passado ao chamar o script

        if sys.argv[1] == "produto":  #se o argumento for produto ele vai entrar no bloco de comando para produto
        #def inserir produto():
            nome = input("Nome do Produto: ")
            cor = input("Cor do Produto: ")
            marca = input("Marca do Produto: ")
            material = input("Material do Produto: ")
            qtd_inventario = int(input("Quantidade em Inventário: "))
            preco = float(input("Preço do Produto: "))
            taxa_iva = float(input("Taxa de IVA (%): "))
            create_produto(nome, cor, marca, material, qtd_inventario, preco, taxa_iva)

        elif sys.argv[1] == "venda":  #se o argumento for venda ele vai entrar no bloco de comando para venda
        #def registar_venda():
            data_venda = input("Data da Venda (YYYY-MM-DD): ")
            hora_venda = input("Hora da Venda (HH:MM:SS): ")
            create_venda(data_venda, hora_venda)
        else:
            print("Argumento inválido!")
    else:
        print("Nenhum argumento transmitido.")

