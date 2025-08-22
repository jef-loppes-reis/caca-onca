"""
    Menu principal
"""
from datetime import datetime

from ecomm_postgres import PostgresConnection

from caca_onca.connection.connection_db import Connection
from caca_onca.use_cases.get_pedidos import GetPedidos

class Main:
    def __init__(self):
        self.connection_master = Connection(PostgresConnection())
        self.get_pedidos = GetPedidos(self.connection_master)

    def _is_date(self, string, date_format="%d/%m/%Y"):
        """
        Verifica se uma string pode ser interpretada como uma data no formato especificado.

        Parâmetros
        ----------
        string : str
            A string a ser validada como data.
        date_format : str, opcional
            O formato esperado da data (padrão: "%d/%m/%Y").

        Retorna
        -------
        bool
            True se a string for uma data válida no formato especificado, False caso contrário.

        Exemplos
        --------
        >>> is_date('22/08/2025')
        True
        >>> is_date('2025-08-22')
        False
        >>> is_date('abc')
        False
        """
        try:
            datetime.strptime(string, date_format)
            return True
        except ValueError:
            return False

    def _convert_date_format(self, date_str, input_format="%d/%m/%Y", output_format="%Y-%m-%d"):
        """
        Converte uma data do formato de entrada para o formato de saída.

        Parâmetros
        ----------
        date_str : str
            A string da data a ser convertida.
        input_format : str, opcional
            O formato da data de entrada (padrão: "%d/%m/%Y").
        output_format : str, opcional
            O formato da data de saída (padrão: "%Y-%m-%d").

        Retorna
        -------
        str
            A data convertida no formato de saída.

        Exemplos
        --------
        >>> _convert_date_format('22/08/2025')
        '2025-08-22'
        """
        try:
            date_obj = datetime.strptime(date_str, input_format)
            return date_obj.strftime(output_format)
        except ValueError:
            return date_str

    def menu(self):
        """
        Menu principal
        """
        while True:
            print("\n" + "="*50)
            print("  CAÇA ONÇA - CONSULTA DE PEDIDOS SEM NOTAS")
            print("="*50)
            print("1 - Consultar pedidos")
            print("2 - Sair")
            print("="*50)
            
            opcao = input("Digite a opção desejada: ")
            
            if not opcao.isnumeric():
                print("❌ Opção inválida! Digite apenas números.")
                continue
                
            opcao = int(opcao)

            if opcao == 2:
                print("👋 Encerrando o sistema...")
                break
            if opcao == 1:
                # Coleta dados para consulta
                codvde = input("Digite o código do vendedor (ex: 7761): ")
                dt_emissao = input("Digite a data de emissão inicial (dd/mm/yyyy): ")
                dt_emissao_fim = input("Digite a data de emissão final (dd/mm/yyyy): ")

                # Validações
                if not codvde:
                    print("❌ Código do vendedor não informado")
                    continue
                if not codvde.isnumeric():
                    print("❌ Código do vendedor inválido - deve conter apenas números")
                    continue
                if not dt_emissao:
                    print("❌ Data de emissão inicial não informada")
                    continue
                if not self._is_date(dt_emissao):
                    print("❌ Data de emissão inicial inválida - use o formato dd/mm/yyyy")
                    continue
                if not dt_emissao_fim:
                    print("❌ Data de emissão final não informada")
                    continue
                if not self._is_date(dt_emissao_fim):
                    print("❌ Data de emissão final inválida - use o formato dd/mm/yyyy")
                    continue

                # Converte datas para formato SQL
                dt_emissao_sql = self._convert_date_format(dt_emissao)
                dt_emissao_fim_sql = self._convert_date_format(dt_emissao_fim)

                params = {
                    'codvde': codvde,
                    'dt_emissao': dt_emissao_sql,
                    'dt_emissao_fim': dt_emissao_fim_sql
                }

                try:
                    print("\n🔍 Consultando pedidos...")
                    df = self.get_pedidos.execute(**params)
                    
                    if df.empty:
                        print("❌ Nenhum pedido encontrado para os critérios informados")
                        continue
                    
                    print(f"✅ Encontrados {len(df)} pedidos!")
                    filename = 'pedidos_sem_notas.xlsx'
                    df.to_excel(filename, index=False)
                    print(f"📊 Relatório salvo como: {filename}")
                    
                except Exception as e:
                    print(f"❌ Erro ao consultar pedidos: {str(e)}")
                    continue
            else:
                print("❌ Opção inválida! Escolha 1 ou 2.")

if __name__ == "__main__":
    main = Main()
    main.menu()
