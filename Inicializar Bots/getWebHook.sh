#!/bin/bash


if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <token_do_bot>"
    exit 1
fi


token_do_bot=$1
curl -X GET "https://api.telegram.org/bot$token_do_bot/getWebhookInfo"



