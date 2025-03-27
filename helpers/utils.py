import os
import os
import json
from datetime import datetime
from dotenv import load_dotenv

def carregar_variaveis_ambiente(caminho_arquivo=".env"):
    if os.path.exists(caminho_arquivo):
        load_dotenv(dotenv_path=caminho_arquivo)
    else:
        load_dotenv()
        print(f"Arquivo .env não encontrado em: {caminho_arquivo}. Usando variáveis do ambiente.")

# Função para converter datetime em string
def convert_datetime(obj):
    """Converte datetime para string formatada."""
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')  # Pode ajustar o formato conforme necessário
    raise TypeError(f"Type {type(obj)} not serializable")

# Função para normalizar datetime dentro de dicionários
def normaliza_dicionario(dicionario):
    """
    Normaliza todos os valores datetime dentro de um dicionário para uma string.
    """
    return {k: convert_datetime(v) if isinstance(v, datetime) else v for k, v in dicionario.items()}

# Função principal para gerenciar a pasta e salvar conteúdo
def gerencia_pasta_processo(path_processo, conteudo_serializado):
    """
    Verifica se uma pasta existe. Caso contrário, cria a pasta.
    Em seguida, chama a função de salvar o conteúdo no arquivo processo.json,
    mas só salva se houver diferenças entre o conteúdo existente e o novo.

    :param path_processo: Caminho da pasta a ser verificada ou criada.
    :param conteudo_serializado: Conteúdo serializado (lista de dicionários) a ser salvo no arquivo processo.json.
    :return: Conteúdo salvo no arquivo processo.json ou mensagem indicando que não houve alterações.
    """
    # Verifica ou cria a pasta
    if not os.path.exists(path_processo):
        os.makedirs(path_processo)
        print(f"Pasta '{path_processo}' criada.")
    else:
        print(f"Pasta '{path_processo}' já existe.")
    
    # Caminho do arquivo processo.json
    print(path_processo, 333)
    path_arquivo = os.path.join(path_processo, "processo.json")
    
    # Chama a função para salvar o conteúdo se houver diferenças
    return salva_conteudo_processo(path_arquivo, conteudo_serializado)

def salva_conteudo_processo(path_arquivo, conteudo_serializado):
    """
    Salva o conteúdo fornecido no arquivo processo.json somente se houver diferenças.

    :param path_arquivo: Caminho completo para o arquivo processo.json.
    :param conteudo_serializado: Lista de dicionários contendo os dados a serem salvos no arquivo JSON.
    :return: Conteúdo salvo ou mensagem de ausência de alterações.
    """
    # Normaliza os datetime para garantir que a comparação seja justa
    conteudo_serializado_normalizado = [normaliza_dicionario(item) for item in conteudo_serializado]
    
    # Verifica se o arquivo existe e se o conteúdo não está vazio
    if os.path.exists(path_arquivo):
        with open(path_arquivo, 'r', encoding='utf-8') as json_file:
            try:
                conteudo_atual = json.load(json_file)
                conteudo_atual_normalizado = [normaliza_dicionario(item) for item in conteudo_atual]
            except json.JSONDecodeError:
                # Caso o arquivo esteja vazio ou corrompido, tratamos a exceção
                print(f"O arquivo '{path_arquivo}' está vazio ou corrompido. Criando novo conteúdo.")
                conteudo_atual_normalizado = []

        # Verifica se o conteúdo é diferente]
        if conteudo_atual_normalizado[0]['setor'] != conteudo_serializado_normalizado[0]['setor'] or conteudo_atual_normalizado[0]['inicio'] != conteudo_serializado_normalizado[0]['inicio']:
            print(f"Conteúdo diferente detectado. Atualizando o arquivo '{path_arquivo}'.")
            with open(path_arquivo, 'w', encoding='utf-8') as json_file:
                json.dump(conteudo_serializado, json_file, indent=4, default=convert_datetime, ensure_ascii=False)
            print(f"Conteúdo atualizado em '{path_arquivo}'.")
            return conteudo_serializado, True
        else:
            print(f"O conteúdo de '{path_arquivo}' já está atualizado. Nenhuma alteração foi feita.")
            return conteudo_atual, False
    else:
        print(f"Arquivo '{path_arquivo}' não existe. Será criado.")
    
    # Salva o novo conteúdo no arquivo
    with open(path_arquivo, 'w', encoding='utf-8') as json_file:
        json.dump(conteudo_serializado, json_file, indent=4, default=convert_datetime, ensure_ascii=False)
    print(f"Conteúdo salvo em '{path_arquivo}'.")
    return conteudo_serializado, True


def monta_path_diretorio(path, processo):
    try:
        dir = os.path.join(path, processo)
        path = os.path.normpath(dir)
        return path
    except Exception as e:
        print('Error: ', e)


