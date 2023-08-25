"""
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(),
QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE
UMA MENSAGEM COM TAMANHO ADAPTÁVEL.

EX:
ESCREVA("OLÁ, MUNDO")
SAÍDA
~~~~~~~~~~~~~
OLÁ, MUNDO
~~~~~~~~~~~~~
"""


def title(titulo):
      str(titulo)
      print('-' * (len(titulo) + 15))
      print(f'{"+" * 5} {titulo} {"+" * 5}')
      print('-' * (len(titulo) + 15))


def escreva(txt):
      print('~' * (len(txt) + 5))
      print(f'{txt:^{len(txt) + 5}}')
      print('~' * (len(txt) + 5))


title('TAMANHO ADAPTAVEL')
escreva(input('Escreva aqui : '))
