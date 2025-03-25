import os
from helpers.utils import carregar_variaveis_ambiente, gerencia_pasta_processo, monta_path_diretorio
import consulta_processo
import notifica
import json
from datetime import datetime
from dotenv import load_dotenv
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Parser'
    )

    parser.add_argument('-e' ,"--email", help="Email do destinatário", required=True)
    parser.add_argument('-n',"--nome", help="Nome do destinatário", required=True)
    parser.add_argument('-p',"--processo", help="Número do processo a acompanhar", required=True)

    args = parser.parse_args()

  
    carregar_variaveis_ambiente(caminho_arquivo='.env')
    BREVO_API_KEY = os.getenv('BREVO_API_KEY')
    path_processos = os.getenv('PATH_ROTINAS')
  
    
    data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f'{data_hora_atual} - Iniciando consulta de processo para o processo de número: {args.processo} - {args.nome}')
    
    processos = consulta_processo.buscar_processo(args.processo)
    tramitacoes_serializaveis = [
            {
                "setor": t.setor,
                "inicio": t.inicio,
                "situacao": t.situacao,
                "tempo_permanencia": t.tempo_permanencia
            }
            for t in processos.tramitacoes
        ]

    # dir = os.path.join(path_processos, args.processo)
    # path = os.path.normpath(dir)
    path = monta_path_diretorio(path_processos, args.processo)

    conteudo, notificar = gerencia_pasta_processo(str(path), tramitacoes_serializaveis)

    if notificar:
        notifica.envia_email(api_key=BREVO_API_KEY, email_destinatario=args.email, n_processo=args.processo, nome_destinatario=args.nome, tramitacao=conteudo[0])
    
    print(f'{data_hora_atual} - Finalizando consulta de processo para o processo de número: {args.processo} - {args.nome}')

