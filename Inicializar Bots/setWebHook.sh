#!/bin/bash

# Verifica se o número correto de parâmetros foi passado
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <token_do_bot> <sua_url>"
    exit 1
fi

# Armazena os parâmetros em variáveis
token_do_bot=$1
sua_url=$2

# Faz a requisição POST para configurar o Webhook do Telegram
curl -X POST "https://api.telegram.org/bot$token_do_bot/setWebhook" -d "url=$sua_url"

# Fim do script

