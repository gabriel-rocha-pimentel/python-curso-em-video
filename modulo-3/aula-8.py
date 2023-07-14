"""
CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS
VALORES NÚMERICOS E CADASTRE-OS EM UMA LISTA.
CASO O NÚMERO JÁ EXISTA LÁ DENTRO, ELE NÃO SERÁ ADICIONADO.
NO FINAL, SERÃO EXIBIDOS TODOS OS VALORES ÚNICOS
DIGITADOS, EM ORDEM CRESCENTE.
"""
print('_' * 50)
print(f'{"+++++ VALORES ÚNICOS +++++":^50}')
print('_' * 50)

# ABAIXO ESTÁ O CODIGO DO ALUNO(EU)
number = list()
while True:
    value = int(input(f'\nDigite um valor : '))
    number.append(value)
    n = number.count(value)
    number.sort()
    if n > 1:
        print('Valor duplicado, não vou adicionar...')
        number.remove(value)
    else:
        print('Valor adicionado com sucesso...')
    opcao = input('Quer continuar ? [SIM | NAO] >>> ').strip().upper()[0]
    if opcao == 'N':
        break
print('-='*20)
print(f'Você digitou os valores {number}')

# LOGO EM SEGUIDA ESTÁ O CODIGO DO PROFESSOR GUANABARA
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar ? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
print(f'Você digitou os valores {numeros}')
