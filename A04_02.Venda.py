import mysql.connector
from sqlalchemy.sql.ddl import DDLIf


class Venda:
    def __init__(self, data_venda, hora_venda):
        self.data_venda = data_venda,
        self.hora_venda = hora_venda

    def set_data_venda(self, data_venda):
        self.data_venda = data_venda

    def set_hora_venda(self, hora_venda):
        self.hora_venda = hora_venda






