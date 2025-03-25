import os
import requests
from datetime import datetime
from constants.entities import Tramitacao

def envia_email(api_key:str, n_processo:str, email_destinatario:str, nome_destinatario:str, tramitacao:Tramitacao):
    remetente = os.getenv('EMAIL_REMETENTE')
    inicio = tramitacao['inicio'].strftime("%d/%m/%Y %H:%M:%S")
    setor = tramitacao['setor']
    situacao = tramitacao['situacao']

    subject = f'{n_processo} - Novas Informações sobre o Seu Processo'
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": f"{api_key}",
        "content-type": "application/json",
    }
    data = {
        "sender": {
            "name": "Atualização Processual CE",
            "email": f"{remetente}",
        },
        "to": [
            {
                "email": f"{email_destinatario}",
                "name": f"{nome_destinatario}",
            }
        ],
        "subject": subject,
        "htmlContent": """
            <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        line-height: 1.5;
                    }
                    .container {
                        max-width: 600px;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    h2 {
                        color: #333;Departamento Financeiro
                    }
                    p {
                        color: #666;
                    }
                </style>
            </head> """ +
            f"""
            <body>
                <div class="container">
                    <h2>Atualização do Seu Processo</h2>
                    <p>Prezado(a) {nome_destinatario},</p>
                    <p>Uma nova tramitação ocorreu em seu processo de número {n_processo}.</p>
                    <p><strong>Situação atual:</strong> {situacao}</p>
                    <p><strong>Setor:</strong> {setor}</p>
                    <p><strong>Última atualização:</strong> {inicio} </p>
                    <p>Surgindo novas atualizações enviaremos um novo e-mail.</p>
                </div>
            </body>
            </html>
        """,
    }

    response = requests.post(url, headers=headers, json=data)

    # Verifica a resposta
    if response.status_code == 200 or response.status_code == 201:
        print("E-mail enviado com sucesso!")
    else:
        print(f"Falha ao enviar o e-mail: {response.status_code}")
        print(response.text)