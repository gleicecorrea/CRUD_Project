from A01_Database import get_db_connection
from A04_01.Produto import
from A04_02.Venda import Venda
from A04_03.DetalheVenda import DetalheVenda
# Listas locais para backup
produtos_local = []
vendas_local = []
detalhes_venda_local = []

def fazer_backup_dados():
    global produtos_local, vendas_local, detalhes_venda_local

    conn = get_db_connection()
    if conn is None:
        print("Falha na conexão com o banco de dados. Não foi possível fazer o backup.")
        return

    try:
        # Backup dos Produtos
        cursor = conn.cursor()
        cursor.execute("SELECT IDProduto, Nome_produto, Cor_produto, Marca_produto, Material_produto, Qtd_inventario, Preco, taxaIVA FROM Produto")
        produtos_local.clear()  # Limpa a lista antes de preencher com dados novos
        for row in cursor.fetchall():
            produto = Produto(
                id_produto=row[0],
                nome=row[1],
                cor=row[2],
                marca=row[3],
                material=row[4],
                qtd_inventario=row[5],
                preco=row[6],
                taxa_iva=row[7]
            )
            produtos_local.append(produto)

        # Backup das Vendas
        cursor.execute("SELECT IDVenda, Data_Venda, Hora_Venda FROM Venda")
        vendas_local.clear()
        for row in cursor.fetchall():
            venda = Venda(
                id_venda=row[0],
                data_venda=row[1],
                hora_venda=row[2]
            )
            vendas_local.append(venda)

        # Backup dos Detalhes da Venda
        cursor.execute("SELECT IDVenda, IDProduto, QuantidadeVendida FROM DetalheVenda")
        detalhes_venda_local.clear()
        for row in cursor.fetchall():
            detalhe_venda = DetalheVenda(
                id_venda=row[0],
                id_produto=row[1],
                quantidade_vendida=row[2]
            )
            detalhes_venda_local.append(detalhe_venda)

        print("Backup realizado com sucesso!")

    except Exception as e:
        print(f"Erro ao realizar o backup: {e}")
    finally:
        cursor.close()
        conn.close()
