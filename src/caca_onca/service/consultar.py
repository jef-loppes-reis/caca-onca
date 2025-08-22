"""Serviço de consulta de dados do banco de dados"""

from pandas import DataFrame

from caca_onca.connection.connection_db import Connection
from caca_onca.connection.queries import query_base

class ConsultarDados:

    def __init__(self, connection: Connection):
        self.connection = connection

    def _get_query(self, **params) -> str:
        return query_base % params

    def execute(self, **params) -> DataFrame:
        query = self._get_query(**params)
        with self.connection as conn:
            return conn.query_string(query)
