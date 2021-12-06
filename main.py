from organizations import Organizations
from download import Downloader
from unzip import Unzipper
from mongodb import MongoDB
from os.path import exists
from datetime import datetime
import csv, json

def get_orgs():
    organizations = Organizations().get_orgs()
    return organizations

def get_file(file_name, url):
    if not exists(f'./files/{file_name}.zip'):
        downloader = Downloader(file_name, url)
        time_elapsed = downloader.download_file()
        print('Download completo...')
        print(f'Tempo decorrido: {time_elapsed}')

def unzip_file(file_name):
    if not exists(f'./csv/{file_name}.csv'):
        unzipper = Unzipper(file_name)
        unzipper.unzip_file()
        print('Arquivo descompactado')

def insert_data(file_name):
    print('Enviando dados para o MongoDB...')
    mongodb = MongoDB()
    with open(f'./json/{file_name}.json', 'w') as outfile:
        json.dump([], outfile)
    with open(f'./csv/{file_name}.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            data = {
                'cnpj_basico': int(row[0]),
                'cnpj_ordem': int(row[1]),
                'cnpj_dv': int(row[2]),
                'identificador': int(row[3]),
                'nome': row[4],
                'situacao': int(row[5]),
                'data_situacao': datetime.strptime(row[6], '%Y%m%d') if len(row[6]) == 6 else row[6],
                'motivo_situacao': int(row[7]),
                'nome_cidade_exterior': row[8],
                'pais': row[9],
                'data_inicial':  datetime.strptime(row[10], '%Y%m%d') if len(row[10]) == 6 else row[10],
                'cnae_princial': row[11],
                'cnae_secundario': row[12],
                'tipo_logradouro': row[13],
                'logradouro': row[14],
                'numero': row[15],
                'complemento': row[16],
                'bairro': row[17],
                'cep': row[18],
                'uf': row[19],
                'municipio': row[20],
                'ddd_1': row[21],
                'telefone_1': row[22],
                'ddd_2': row[23],
                'telefone_2': row[24],
                'ddd_fax': row[25],
                'fax': row[26],
                'email': row[27],
                'situacao_especial': row[28],
                'data_situacao_especial': row[29],
            }
            mongodb.insert(data)

def __main__():

    organizations = get_orgs()
    print('Dados públicos do CNPJ disponíveis para download:\n')
    for index, organization in enumerate(organizations):
        name = organization['name']
        print(f'{index} - {name}')

    option = int(input('\nDigite o número da opção desejada: '))
    if option < 0 or option > len(organizations):
        print('Opção inválida')
        return

    organization = organizations[option]
    file_name = organization['name']

    get_file(file_name, organization['url'])

    unzip_file(file_name)

    insert_data(file_name)

__main__()
