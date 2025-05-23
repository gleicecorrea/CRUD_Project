import mysql.connector


class DetalheVenda:
    def __init__(self, id_venda, id_produto, quantidade_vendida):
        self.id_venda = id_venda
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida

    def save(self, cursor):
        cursor.execute("""
            INSERT INTO DetalheVenda (IDVenda, IDProduto, QuantidadeVendida)
            VALUES (%s, %s, %s)
        """, (self.id_venda, self.id_produto, self.quantidade_vendida))

    @staticmethod
    def list_all(cursor):
        cursor.execute("SELECT * FROM DetalheVenda")
        return cursor.fetchall()

    @staticmethod
    def vendas_por_produto(cursor, id_produto):
        cursor.execute("""
            SELECT * FROM DetalheVenda
            WHERE IDProduto = %s
        """, (id_produto,))
        return cursor.fetchall()
