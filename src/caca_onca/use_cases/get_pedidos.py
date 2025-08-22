"""Use case de consulta de pedidos"""
from ecomm_postgres import PostgresConnection
from pandas import DataFrame

from caca_onca.connection.connection_db import Connection
from caca_onca.service.consultar import ConsultarDados

class GetPedidos:

    def __init__(self, connection: Connection):
        self.consultar_dados = ConsultarDados(connection)

    def execute(self, **params) -> DataFrame:
        return self.consultar_dados.execute(**params)

if __name__ == "__main__":
    connection_master = Connection(PostgresConnection())
    get_pedidos = GetPedidos(connection_master)
    print(get_pedidos.execute(codvde='7761', dt_emissao='2025-08-01', dt_emissao_fim='2025-08-22'))

