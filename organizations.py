import requests
from bs4 import BeautifulSoup

class Organizations:
    """
    This class is used to get the organizations from the
    organizations page.
    """

    def __init__(self):
        """
        This is the constructor for the Organizations class.
        """
        self.url = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'
        self.orgs = []

    def get_orgs(self):
        """
        This method is used to get the organizations from the
        organizations page.
        """
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        orgs = soup.find_all('a', {'class': 'external-link'}, href=True)
        for org in orgs:
            data = {'name': org.text, 'url': org['href']}
            if 'ESTABELECIMENTO ' in data['name']:
                self.orgs.append(data)
        return self.orgs