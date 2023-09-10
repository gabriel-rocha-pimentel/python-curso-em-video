"""
FAÇA UM MINI-SISTEMA QUE UTILIZE O
INTERECTIVE HELP DO PYTHON. O USUÁRIO
VAI DIGITAR UM COMANDO E O MANUAL VAI APARECER.

QUANDO O USURÁRIO DIGITAR A PALAVRA 'FIM',
O PROGRAMA SE ENCERRARÁ.

OBS: USE CORES
"""


def biblioteca(software):
      print(f'\033[47m')
      help(software)
      print(f'\033[0;0m')


# PROGRAMA PRINCIPAL
print(f'\033[32m{"+" * 30} {"SISTEMA DE AJUDA PyHELP":^30} {"+" * 30}\033[0;0m')
fim = True
while fim:
      book_func = input(f'\033[32mFunção ou Biblioteca > \033[0;0m')
      if book_func.upper().strip() == 'FIM':
            fim = False
      else:
            print(biblioteca(book_func))
