from bs4 import BeautifulSoup
import requests

class RemoteImport:
    def __init__(self):
        print('initialized')


    def pypi_find(self, query):
        ENDPOINT = 'https://pypi.org/search/'
        payload = {'q': query}
        resp = requests.get(ENDPOINT, params=payload)
        soup = BeautifulSoup(resp.content, features='lxml')
        results = soup.find_all('ul', {'class': 'unstyled'})
        results = [i.find_all('li') for i in results][0]

        package_names = [i.find(
            'span', {'class': 'package-snippet__name'}
            ).text for i in results]
        package_vers = [i.find(
            'span', {'class': 'package-snippet__version'}
            ).text for i in results]

        result = list(zip(package_names, package_vers))
        result = '\n'.join([' '.join(i) for i in result])

        print('Query: {}\n----------\nFound:\n{}'.format(query, result))


    def pypi_import(search, package):
        os.system('pip install {}'.format(package))


importer = RemoteImport()
importer.pypi_find(input('find: '))
# importer.pypi_import()
