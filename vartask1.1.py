from bs4 import BeautifulSoup
import requests

class RemoteImport:
    def __init__(self):
        pass

    def pypi_find(self, query):
        ENDPOINT = 'https://pypi.org/search/'
        payload = {'q': query}
        resp = requests.get(ENDPOINT, params=payload)
        soup = BeautifulSoup(resp.content, features='lxml')
        results = soup.find_all('ul', {'class': 'unstyled'})
        results = [i.find_all('li') for i in results][0]

        pkg = 'package-snippet_'

        package_names = [i.find('span', {'class': f'{pkg}_name'}).text for i in results]
        package_vers =[i.find('span', {'class': f'{pkg}_version'}).text for i in results]

        result = list(zip(package_names, package_vers))
        result = '\n'.join([f'{i[0]} {i[1]}' for i in result])

        print(f'''Query: {query}
----------
Found:
{result}''')

    def pypi_import(search, package):
        os.system('pip install {package}')


importer = RemoteImport()
importer.pypi_find(input('find: '))
# importer.pypi_import('')