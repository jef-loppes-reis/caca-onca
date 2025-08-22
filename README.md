# 🐆 Caça Onça - Sistema de Consulta de Pedidos Sem Notas

Sistema para consulta de pedidos que ainda não possuem notas fiscais emitidas, facilitando o controle e acompanhamento de pendências.

## 📋 Pré-requisitos

Antes de usar o sistema, certifique-se de que possui:

- **Python 3.13+** instalado
- **UV (UltraViolet)** instalado e configurado no PATH
- **Acesso ao banco de dados PostgreSQL** com as credenciais corretas
- **Conexão com a internet** para instalação de dependências

### Instalação do UV

Se ainda não possui o UV instalado:

1. Visite: https://github.com/astral-sh/uv
2. Siga as instruções de instalação para Windows
3. Certifique-se de que o UV está no PATH do sistema

## 🚀 Como Usar

### Execução Rápida

1. **Abra o terminal** no diretório do projeto
2. **Execute o arquivo batch:**
   ```cmd
   .\rodar_caca_onca.bat
   ```
3. **Siga as instruções** no menu interativo

### Menu do Sistema

O sistema apresentará o seguinte menu:

```
==================================================
  CAÇA ONÇA - CONSULTA DE PEDIDOS SEM NOTAS
==================================================
1 - Consultar pedidos
2 - Sair
==================================================
```

### Realizando uma Consulta

Para fazer uma consulta de pedidos:

1. **Digite `1`** para consultar pedidos
2. **Informe os dados solicitados:**
   - **Código do vendedor** (ex: 7761)
   - **Data inicial** no formato dd/mm/yyyy (ex: 01/08/2025)
   - **Data final** no formato dd/mm/yyyy (ex: 22/08/2025)

3. **Aguarde o processamento** - o sistema irá:
   - Conectar ao banco de dados
   - Executar a consulta
   - Gerar o relatório em Excel

4. **Verifique o resultado:**
   - Se encontrar pedidos: arquivo `pedidos_sem_notas.xlsx` será criado
   - Se não encontrar: mensagem informativa será exibida

## 📊 Relatório Gerado

O sistema gera um arquivo Excel (`pedidos_sem_notas.xlsx`) contendo as seguintes informações:

| Campo | Descrição |
|-------|-----------|
| **loja** | Nome da loja (PECISTA, KAIZEN, etc.) |
| **numero_pedido** | Número do pedido |
| **serie_pedido** | Série do pedido |
| **data_emissao** | Data de emissão do pedido |
| **hora_emissao** | Hora de emissão do pedido |
| **natureza_pedido** | Natureza da operação |
| **tipo_pedido** | Tipo do pedido |
| **codigo_cliente** | Código do cliente |
| **codigo_vendedor** | Código do vendedor |
| **valor_total_pedido** | Valor total do pedido |
| **forma_pagamento** | Forma de pagamento |
| **observacao_linha1** | Primeira linha de observação |
| **observacao_linha2** | Segunda linha de observação |
| **observacao_linha3** | Terceira linha de observação |
| **numero_nota** | Número da nota fiscal (NULL para pedidos sem nota) |
| **serie_nota** | Série da nota fiscal (NULL para pedidos sem nota) |
| **cancelado** | Status de cancelamento (N/S) |

## ⚙️ Configuração do Banco de Dados

O sistema utiliza as configurações do módulo `ecomm-postgres`. Certifique-se de que:

- As variáveis de ambiente estão configuradas corretamente
- A conexão com o banco PostgreSQL está funcionando
- O usuário possui permissões de leitura na tabela `"D-1".pedido`

## 🔧 Resolução de Problemas

### Erro: "UV não encontrado"
- Instale o UV seguindo as instruções oficiais
- Verifique se está no PATH do sistema
- Reinicie o terminal após a instalação

### Erro: "Arquivo main.py não encontrado"
- Certifique-se de executar o script no diretório correto
- Verifique se a estrutura de pastas está intacta

### Erro de conexão com banco
- Verifique as credenciais do banco de dados
- Confirme se o serviço PostgreSQL está rodando
- Teste a conectividade de rede

### Erro: "Data inválida"
- Use sempre o formato dd/mm/yyyy
- Exemplo correto: 22/08/2025
- Exemplos incorretos: 2025-08-22, 22-08-2025

### Arquivo Excel não é gerado
- Verifique se há pedidos no período consultado
- Confirme se possui permissões de escrita no diretório
- Certifique-se de que o Excel não está aberto com o arquivo

## 🏗️ Estrutura do Projeto

```
caca-onca/
├── src/
│   └── caca_onca/
│       ├── app/
│       │   └── main.py          # Interface principal
│       ├── connection/
│       │   ├── connection_db.py # Conexão com banco
│       │   └── queries.py       # Consultas SQL
│       ├── service/
│       │   └── consultar.py     # Serviço de consulta
│       └── use_cases/
│           └── get_pedidos.py   # Caso de uso principal
├── rodar_caca_onca.bat         # Script de execução
├── pyproject.toml              # Configurações do projeto
└── README.md                   # Este arquivo
```

## 📝 Logs e Monitoramento

O sistema exibe logs informativos durante a execução:

- ✅ **Sucesso:** Conexões estabelecidas e operações bem-sucedidas
- ❌ **Erro:** Problemas de conexão ou validação
- 🔍 **Info:** Informações sobre o processo de consulta

## 🆘 Suporte

Em caso de problemas ou dúvidas:

1. Verifique se seguiu todos os pré-requisitos
2. Consulte a seção "Resolução de Problemas"
3. Verifique os logs exibidos no terminal
4. Entre em contato com a equipe de desenvolvimento

---

**Versão:** 1.0.0  
**Desenvolvido por:** jef-loppes-reis  
**Email:** jefersondip25@gmail.com

---

*Sistema desenvolvido para facilitar o controle e acompanhamento de pedidos pendentes de faturamento.*
