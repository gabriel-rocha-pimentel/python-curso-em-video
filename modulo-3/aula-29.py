"""
CRIE UM PROGRAMAM QUE TENHA UMA FUNÇÃO
CHAMADA VOTO(), QUE VAI RECEBER COMO PARÂMETRO
O ANO DE NASCIMENTO DE UMA PESSOA,
RETORNANDO UM VALOR LITERAL INDICANDO
SE UMA PESSOA TEM VOTO NEGADO, OPCIONAL
OU OBRIGATÓRIO NAS ELEIÇÕES.
"""


def voto(ano=2000):
      from datetime import datetime
      ano_atual = datetime.today().year
      idade = ano_atual - ano
      print(f'Com {idade} anos: ', end='')
      if 18 <= idade < 60:
            print('VOTO OBRIGATÓRIO.')
      elif 16 <= idade <= 18 or idade >= 60:
            print('VOTO OPCIONAL')
      else:
            print('NÃO VOTA')


# PROGRAMA PRINCIPAL
voto(int(input('Em que ano você nasceu?\n>>> ')))
