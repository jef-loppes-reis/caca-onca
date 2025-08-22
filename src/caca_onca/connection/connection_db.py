"""Conexão com o banco de dados"""

from ecomm_postgres import PostgresConnection

class Connection:

    def __init__(self, connection: PostgresConnection):
        self.connection = connection
    
    def __enter__(self):
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
