"""
CRIE UM PROGRAM AQUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO.
NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES
E QUAL FOI O MAIOR E O MENOR VALOR LIDO. O PROGRAMA DEVE PERGUNTAR
AO USÚARIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.
"""

print('*{}*\n '
      '\t\t\t\t\t\t\t\t MAIOR E MENOR VALOR'
      '\n*{}*'.format('-+-' * 30, '-+-' * 30))
saida = False
n1 = num = soma = media = 0
lista = []
while not saida:
      num = int(input('\nDigite um número : '))
      lista += [num]
      soma += num
      n1 += 1
      opcao = input('Quer continuar [N | S] >>> ').upper()

      if opcao == 'S':
            continue
      elif opcao == 'N':
            saida = True
      else:
            print('Opção invalida')
      media = soma / n1

print('\nVocê digitou {} números. E a média foi {:.2f}'.format(n1, media))
print('O maior valor foi {} e o menor {}.'.format(max(lista), min(lista)))
