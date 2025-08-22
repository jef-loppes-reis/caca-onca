@echo off
title Caca Onca - Sistema de Consulta de Pedidos Sem Notas

echo ================================================
echo   Caca Onca
echo   Versao 1.0.0
echo   Sistema de Consulta de Pedidos Sem Notas
echo ================================================
echo.

:: Verifica se o UV esta instalado
uv --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] UV nao encontrado no sistema!
    echo Por favor, instale o UV e adicione-o ao PATH.
    echo.
    pause
    exit /b 1
)

echo [INFO] UV encontrado - verificando ambiente...

:: Verifica se o arquivo main.py existe
if not exist "src/caca_onca/app/main.py" (
    echo [ERRO] Arquivo main.py nao encontrado!
    echo Certifique-se de executar no diretorio correto.
    echo.
    pause
    exit /b 1
)

echo [INFO] Arquivo main.py encontrado.

:: Instala dependencias
echo [INFO] Instalando dependencias...
uv pip install -e . >nul 2>&1

echo [INFO] Iniciando Caca Onca...
echo ================================================
echo.

uv run src/caca_onca/app/main.py

:: Captura o código de saída do Python
set PYTHON_EXIT_CODE=%ERRORLEVEL%

echo.
echo ================================================

:: Verifica se houve erro
if %PYTHON_EXIT_CODE% neq 0 (
    echo [ERRO] O programa terminou com codigo de erro: %PYTHON_EXIT_CODE%
    echo.
    echo Para debug, verifique:
    echo 1. Se todas as dependencias estao instaladas: uv pip install -e .
    echo 2. Se as configuracoes de banco de dados estao corretas
    echo 3. Se os tokens de API estao validos
    echo 4. Se ha conexao com a internet
    echo.
    color 4F
    echo PRESSIONE QUALQUER TECLA PARA FECHAR...
    pause >nul
) else (
    echo [SUCESSO] Programa executado com sucesso!
    echo.
    color 2F
    echo Pressione qualquer tecla para fechar...
    pause >nul
)

:: Restaura cor original
color

exit /b %PYTHON_EXIT_CODE% 
