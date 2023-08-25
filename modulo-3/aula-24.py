"""
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA().
QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR
(LARGURA E COMPRIMENTO) E MOSTRE A ÁREA DO TERRENO.
"""


def calc_area(larg, comp):
      A = larg * comp
      return print(f'A área de um terreno {larg}x{comp} é de {A}²')


def title(titulo):
      str(titulo)
      print('-' * (len(titulo) + 15))
      print(f'{"+" * 5} {titulo} {"+" * 5}')
      print('-' * (len(titulo) + 15))


title('CONTROLE DE TERRENOS')
largura = int(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calc_area(largura, comprimento)
