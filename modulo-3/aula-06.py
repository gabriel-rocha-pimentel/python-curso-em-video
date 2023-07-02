"""
CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS.
DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS
SÃO AS SUAS VOGAIS.
"""
print('_' * 50)
print(f'{"+++++ LISTAGEM DE PREÇOS +++++":^50}')
print('_' * 50)
# ABAIXO ESTÁ A SOLUÇÃO DO ALUNO
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    vogal_A = palavra.count('A')
    vogal_E = palavra.count('E')
    vogal_I = palavra.count('I')
    vogal_O = palavra.count('O')
    vogal_U = palavra.count('U')

    print(f'Na palavra {palavra} temos '
          f'{vogal_A * "a", vogal_E * "e", vogal_I * "i", vogal_O * "o", vogal_U * "u"}')

# LOGO EM SEGUIDA A SOUÇÃO DO PROFESSOR GUANABARA
print('\n\n')
print('_' * 50)
print(f'{"+++++ SOLUÇÃO DO PROFESSOR +++++":^50}')
print('_' * 50)

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')

    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end='')
