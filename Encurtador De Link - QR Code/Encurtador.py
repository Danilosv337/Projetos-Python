import urllib
import requests
key = '138bd3cbebc6c9c03e788185d8def531871bd'

URL = input('Digite o link que voce deseja encurtar...')
NAME =  input('Digite Um nome personalizado para a URL')
url = urllib.parse.quote(f'{URL}')
name  = f'{NAME}'
r = requests.get(f'http://cutt.ly/api/api.php?key={key}&short={url}&name={name}')

print(r.text)