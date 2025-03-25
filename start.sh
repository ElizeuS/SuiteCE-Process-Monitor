#!/bin/bash

# Define o caminho do arquivo JSON
json_file="usuarios.json"

# Usa jq para iterar pelos objetos e extrair nome e email
jq -c '.[]' "$json_file" | while read -r item; do
  NOME=$(echo "$item" | jq -r '.nome')
  EMAIL=$(echo "$item" | jq -r '.email')
  PROCESSO=$(echo "$item" | jq -r '.processo')

  #Criar diretório para o proceso
  mkdir -p /app/processos/$PROCESSO

  echo "*/5 * * * 1-5 root /bin/bash -c \"/usr/local/bin/python3 /app/main.py  -n '$NOME' -e '$EMAIL' -p '$PROCESSO' >> /app/processos/${PROCESSO}/logs.log 2>&1\"" > /etc/cron.d/notifica-att-processo

done

# Dar permissão ao arquivo de cron
chmod 0644 /etc/cron.d/notifica-att-processo

# Aplicar as tarefas do cron
crontab /etc/cron.d/notifica-att-processo

# Iniciar o cron em foreground
cron -f