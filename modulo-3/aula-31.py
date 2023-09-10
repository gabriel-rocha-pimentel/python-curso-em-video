"""
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO
CHAMADA FICHA(), QUE RECEBA DOIS PARÂMETROS
OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS
ELE MARCOU

O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA
DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO
INFORMADO CORRETAMENTE.
"""


def ficha(jogador='<jogador_desconhecido>', gol=0):
      print(f'O jogador {jogador} fez {gol} gol(s) no campeonato')


# PROGRAMA PRINCIPAL
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
      gols = int(gols)
else:
      gols = 0
if nome.strip() == '':
      ficha(gol=gols)
else:
      ficha(nome, gols)
