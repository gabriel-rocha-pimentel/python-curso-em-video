"""
CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE
PUDIM ESTPA ACESSIVEL PEÇO COMPUTADOR USADO.
"""
import requests

myWeb = {'google': 'https://www.google.com.br',
         'pudim': 'https://www.pudim.com.br',
         'imperador nerd': 'https://www.imperadornerd.com.br',
         'youtube': 'https://www.youtube.com.br'}

for name, url in myWeb.items():
      try:
            statusCode = requests.get(url)
      except:
            print(f'O site {name} está fora do ar!!!')
      else:
            print(f'O site {name} está funcionando normalmente')
