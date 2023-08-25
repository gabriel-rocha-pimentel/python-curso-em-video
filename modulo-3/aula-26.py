"""
FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO
CHAMADA CONTADOR(), QUE RECEBA TRÊS PARâMETROS
INICIO, FIM E PASSO E REALIZE A CONTAGEM.

SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS
ATRAVÉS DA FUNÇÃO CRIADA:

A - DE 1 ATÉ 10, DE 1 EM 1
B- DE 10 ATÉ 0, DE 2 EM 2
C - UMA CONTAGEM PERSONALIDA.
"""
from operator import neg


def title(titulo):
      str(titulo)
      print('-' * (len(titulo) + 15))
      print(f'{"+" * 5} {titulo} {"+" * 5}')
      print('-' * (len(titulo) + 15))


def contador(inicio, fim, passo):
      print('-=' * 50)

      if inicio < fim:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

            for count in range(inicio, fim + 1, passo):
                  print(f'{count}', end=' ')
            print('FIM!')
      else:
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

            if not fim:
                  for count in range(inicio, neg(fim) - 1, passo):
                        print(f'{count}', end=' ')
                  print('FIM!')
            else:
                  for count in range(inicio, fim - 1, neg(passo)):
                        print(f'{count}', end=' ')
                  print('FIM!')
      print('-=' * 50)


# PROGRAMA PRINCIPAL
title('FUNÇÃO CONTADOR')

contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')

num_start = int(input('Início: '))
num_end = int(input('Fim: '))
num_pass = int(input('Passo: '))

print('-=' * 50)
contador(num_start, num_end, num_pass)

# CÓDIGO DO PROFESSOR GUANABARA
"""
from time import sleep


def contador(i, f, p):
      if p < 0:
            p *= -1
      if p == 0:
            p = 1
      print('-=' * 20)
      print(f'Contagem de {i} até {f} de {p} em {p}')
      sleep(2.5)

      if i < f:
            count = i
            while count <= f:
                  print(f'{count} ', end='', flush=True)
                  sleep(0.5)
                  count += p
            print('FIM!')
      else:
            count = i
            while count >= f:
                  print(f'{count} ', end='', flush=True)
                  sleep(0.5)
                  count -= p
            print('FIM!')


# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inínio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
"""
