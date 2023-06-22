"""
CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:

1 SOMAR
2 MULTIPLICAR
3 MAIOR
4 NOVOS NÚMEROS
5 SAIR DO PROGRAMA

SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.
"""

print('*{}*\n '
      '\t\t\t\t\t\t\t\t MENU COM OPÇÕES'
      '\n*{}*'.format('-+-' * 30, '-+-' * 30))

start = input('Escreva [START] para iniciar o program >>> ').upper()

if start == 'START':
      soma = 0
      mult = 0
      opcao = 0

      num1 = int(input('\nPrimeiro valor : '))
      num2 = int(input('Segundo valor : '))

      while opcao != 5:
            print('*{}*  ESCOLHA  *{}*'.format('-+-' * 10, '-+-' * 10))
            opcao = int(input(
                  '[1] SOMAR\n'
                  '[2] MULTIPLICAR\n'
                  '[3] MAIOR\n'
                  '[4] NOVOS NÚMEROS\n'
                  '[5] SAIR DO PROGRAMA\n'
                  '>>> SUA OPÇÃO : '))

            if opcao == 1:
                  soma = num1 + num2
                  print('\nA soma de {} + {} é igual a {}.\n{}'.format(num1, num2, soma, '-+-' * 20))

            elif opcao == 2:
                  mult = num1 * num2
                  print('\nA multiplicação de {} x {} é igual a {}.\n{}'.format(num1, num2, mult, '-+-' * 20))

            elif opcao == 3:
                  if num1 >= num2:
                        maior = num1
                  else:
                        maior = num2
                  print('\nEntre {} e {} o maior número é {}.\n{}'.format(num1, num2, maior, '-+-' * 20))

            elif opcao == 4:
                  num1 = int(input('\nPrimeiro valor : '))
                  num2 = int(input('Segundo valor : '))

            elif opcao == 5:
                  continue
            else:
                  print('Opção invalida. Tente novamente!!')
      print('Você saíu do programa.')

elif start != 'START':
      print('Opção invalida!!! TENTE NOVAMENTE')
