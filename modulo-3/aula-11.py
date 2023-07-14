"""
CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS
E COLOCAR EM UMA LISTA.
DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER
APENAS OS VALORES PARES E OS VALORES IMPARES DIGITADOS,
RESPECTIVAMENTE. AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS.
"""
print('_' * 50)
print(f'{"+++++ DIVIDINDO VALORES +++++":^50}')
print('_' * 50)

numeros = list()
numero_par = list()
numero_impar = list()

while True:
      numero = int(input('\nEscreva um número : '))
      resp = input('Quer continuar ? [SIM ou NÃO]\n>>> ').strip().upper()[0]
      numeros.append(numero)
      if numero % 2 == 0:
            numero_par.append(numero)
      else:
            numero_impar.append(numero)

      if resp == 'N':
            break
print('-=' * 30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {numero_par}')
print(f'A lista de ímpares é {numero_impar}')
