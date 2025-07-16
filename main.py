import os
import requests
from dotenv import load_dotenv
from condominios import condominios
from datetime import datetime


load_dotenv()
app_token = os.getenv('APP_TOKEN')
access_token = os.getenv('ACCESS_TOKEN')

def get_id_relatorio(id_condomino):
    headers = {
        'app_token': app_token,
        'access_token': access_token
    }

    params = {
        'ID_CONDOMINIO_COND': id_condomino,
        'render': 'pdf',
        'getId': 1,
        'PERIODO': -1,
        'Baixar': 1
    }

    response = requests.get('https://api.superlogica.net/v2/condor/relatorios/id/065A',
    headers=headers,
    params=params
    )

    response.raise_for_status()
    id_impressao = response.json()[0]['id_impressao']
    return id_impressao

def get_link_download(id_impressao):
    headers = {
        'app_token': app_token,
        'access_token': access_token
    }

    params = {
        'FL_COMPARTILHAR': 1,
        'ID_IMPRESSAO_FIMP': id_impressao   
    }

    response = requests.get('https://api.superlogica.net/v2/condor/impressoes/post',
    headers=headers, 
    params=params                       
    )

    response.raise_for_status()
    link_download = response.json()[0]['data']['link_externo']
    return link_download

def salvar_pdf(link_download, nome, sigla):
    nome_condominio = f'{nome} ({sigla})'
    caminho = f'G:/Meu Drive/CONDOMÍNIOS/{nome_condominio}/FINANCEIRO/CONTAS/'
    hoje = datetime.today()
    mes = hoje.month -1 or 12
    ano = hoje.year if hoje.month > 1 else hoje.year - 1
    data_formatada = f'{ano}-{mes:02}'

    
    nome_arquivo = f'{data_formatada} DESPESAS BANCÁRIAS {sigla}.pdf'
    response = requests.get(link_download)
    response.raise_for_status()
    with open(f'{caminho}/{nome_arquivo}', 'wb') as f:
        f.write(response.content)
    print(f"PDF salvo com sucesso: {nome_condominio} - {nome_arquivo}")

    
def processar_condominio(id_condomino, nome, sigla):
    id_impressao = get_id_relatorio(id_condomino)
    link_download = get_link_download(id_impressao)
    salvar_pdf(link_download, nome, sigla)
    

def main():
    for condominio in condominios:
        id_condomino = condominio['id']
        nome = condominio['nome']
        sigla = condominio['SIGLA']
        processar_condominio(id_condomino, nome, sigla)

if __name__ == "__main__":
    main()