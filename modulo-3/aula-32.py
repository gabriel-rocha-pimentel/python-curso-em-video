"""
CRIE UM PROGRAMA QUE TENHA A FUNÇÃO LEIAINT(),
QUE VAI FUNCIONAR DE FORMA SEMELHANTE Á FUNÇÃO
INPUT() DO PYTHON, SÓ QUE FAZENDO A VALIDAÇÃO
PARA ACEIRTAR APENAS UM VALOR NUMÉRICO.

EX:
N = LEIAINT('DIGITE UM N')
"""


def leiaInt(num):
      while not num.isnumeric():
            num = input('Digite um número: ')
            if not num.isnumeric():
                  print('\033[0;31mERROR! Digite um número inteiro válido.\033[m')

      return num


# PROGRAMA PRINCIPAl
n = leiaInt("Digite um número: ")
print(f'Você acabou de digitar o número {n}')
