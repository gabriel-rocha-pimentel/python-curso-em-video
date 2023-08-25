"""
FAÇA UM PROGRAMA QUE TENHA UMA LISTA
CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS
SORTEIO() E SOMAPar().

A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS
E VAI COLOCA-LOS DENTRO DA LISTA E A SEGUNDA
FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES
SPRTEADOS PELA FUNÇÃO ANTERIOR
"""
from random import randint


def title(titulo):
      str(titulo)
      print('-' * (len(titulo) + 15))
      print(f'{"+" * 5} {titulo} {"+" * 5}')
      print('-' * (len(titulo) + 15))


def sorteio():
      numeros = list()
      for num in range(0, 5):
            numSort = randint(0, 10)
            numeros.append(numSort)
      return numeros


def somaPar(*num):
      soma = 0
      for value in num:
            for count in value:
                  if count % 2 == 0:
                        soma += count
      return soma


# PROGRAMA PRINCIPAL

title('SORTEAR E SOMAR')
sort = sorteio()

print(f'Sorteando {len(sort)} valores da lista: ', end='')
for n in sort:
      print(n, end=' ')
print('PRONTO!')

print(f'Somando os valores pares de {sort}, temos {somaPar(sort)}')
