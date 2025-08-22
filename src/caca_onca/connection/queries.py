"""Consulta de dados do banco de dados"""

query_base: str = '''
    SELECT
        CASE
            WHEN pedido.cd_loja = '01' THEN 'PECISTA'
            WHEN pedido.cd_loja = '02' THEN '02'
            WHEN pedido.cd_loja = '03' THEN 'KAIZEN ASANORTE'
            WHEN pedido.cd_loja = '04' THEN 'KAIZEN CEILANDIA'
            WHEN pedido.cd_loja = '05' THEN 'KAIZEN GAMA'
            WHEN pedido.cd_loja = '06' THEN 'KAIZEN SOF'
            WHEN pedido.cd_loja = '07' THEN 'KAIZEN PLANALTINA'
            WHEN pedido.cd_loja = '08' THEN 'KAIZEN GOIANIA'
        ELSE 'OUTROS'
        END as loja,
        pedido.nu_nota as numero_pedido,
        pedido.serie as serie_pedido,
        pedido.dt_emissao as data_emissao,
        pedido.hr_emissao as hora_emissao,
        pedido.natureza as natureza_pedido,
        pedido.tipo as tipo_pedido,
        pedido.codcli as codigo_cliente,
        pedido.codvde as codigo_vendedor,
        pedido.valor_tot as valor_total_pedido,
        pedido.forma_pgto as forma_pagamento,
        pedido.observa as observacao_linha1,
        pedido.observa2 as observacao_linha2,
        pedido.observa3 as observacao_linha3,
        pedido.numnota as numero_nota,
        pedido.sernota as serie_nota,
        pedido.cancelada as cancelado
        FROM
            "D-1".pedido
    WHERE 
        codvde = '%(codvde)s' AND
        numnota IS NULL AND
        dt_emissao BETWEEN '%(dt_emissao)s' AND '%(dt_emissao_fim)s'
    '''
