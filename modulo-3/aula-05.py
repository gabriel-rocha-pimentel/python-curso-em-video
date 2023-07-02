"""
CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS
E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA:

- NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOSM ORGANIZANDO OS DADOS
EM FORMA TABULAR.
"""
# SEGUE ABAIXO O CODIGO DO ALUNO GABRIEL(EU).
print('_' * 50)
print('\t\t\t++++++ LISTAGEM DE PREÇOS ++++++')
print('_' * 50)

produtos = ('Lápis', 'Borracha', 'Caderno', 'Estojo',
            'Transferidor', 'Compasso', 'Mochila', 'Canetas',
            'Livro')
valores = (1.75, 2.00, 15.90, 25.00, 4.20,
           9.99, 120.32, 22.30, 34.90
           )
ponto = '.'
value = 0
for produto in produtos:
    for valor in valores:
        value = valor
    print(f'{produto:12}{ponto*25}R$', end=' ')
    print(f'{value:.2f}')
print('_'*50)

print(f'\n{"ABAIXO ESTÁ O CÓDIGO DO PROFESSOR":^40}')
# E LOGO ABAIXO O CODIGO DO PROFESSOR GUANABARA DO CURSA EM VIDEO
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('_' * 40)
