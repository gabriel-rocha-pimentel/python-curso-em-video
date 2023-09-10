"""
CRIE UM PROGRAMAM QUE TENHA UMA FUNÇÃO
FATORIAL() QUE RECEBA DOIS PARÂMETROS:
O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR
E O OUTRO CHAMADO SHOW, QUE SERÁ UM VALOR LÓGICO
(OPCIONAL) INDICANDO SE SERÁ MOSTRADO OU NÃO
NA TELA O PROCESSO DE CÁLCULO DA FATORIAL.
"""


def fatorial(num, show=False):
      """
      :param num:
      :param show:
      :return: 5 x 4 x 3 x 2 x 1 = 120

      Programa calculador de fatorial., siga o exemplo
      e obtenha o resultado. True para ve-lo completo,
      False para ver apenas o valor da fatorial.
      """
      fat = 1
      count = num
      print('_' * 30)

      if show:
            for n in range(num, 0, -1):
                  if n >= 2:
                        fat *= n
                        print(f'{count}', end=' x ')
                        count -= 1
            print(f'1 = {fat}')
      else:
            for n in range(num, 0, -1):
                  if n >= 2:
                        fat *= n
            print(f'{fat}')


fatorial(5, True)
help(fatorial)
