"""
FAÇA UM PROGRAMA QUE TENHA UMA
FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS
PARAMETROS COM VALORES INTEIROS.

SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES
E DIZER QUAL DELES É O MAIOR.
"""


def title(titulo):
      str(titulo)
      print('-' * (len(titulo) + 15))
      print(f'{"+" * 5} {titulo} {"+" * 5}')
      print('-' * (len(titulo) + 15))


def max_min_values(*numeros):
      global menor, maior
      c = 0
      for num in numeros:

            if c == 0:
                  maior = menor = num
            else:
                  if num > maior:
                        maior = num

                  if num < menor:
                        menor = num

            c += 1

      print('\nAnalisando os valores passados...')
      print(f'{numeros}Foram informados {len(numeros)} valores ao todo')
      print(f'O maior valor informardo foi {maior}')
      print('-=' * 30)


# PROGRAMA PRINCIPAL
title('FUNÇÃO MAIOR E MENOR ')
max_min_values(2, 9, 4, 5, 7, 1)
max_min_values(4, 7, 0)
max_min_values(1, 2)
max_min_values(6)
max_min_values(0)
