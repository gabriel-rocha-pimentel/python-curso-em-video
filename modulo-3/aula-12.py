"""
CRIE UM PROGAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO
QUALQUER QUE USE PARÊNTESES. SEU APLICATIVO DEVERÁ
ANALISAR SE A EXPRESSÃO PASSADA ESTÁ COM OS PARÊNTESES
ABERTOS E FECHADOS NA ORDEM CORRETA.
"""
print('_' * 50)
print(f'{"+++++ VALIDANDO EXPRESSÕES +++++":^50}')
print('_' * 50)

expressao = str(input('Escreva a sua expressão : ')).strip()
parentese = 0

for letra in expressao:
      if letra == '(' or letra == ')':
            parentese += 1

if parentese % 2 == 0:
      print('Sua expressão está válida !')
else:
      print('Sua expressão está invalida !')
