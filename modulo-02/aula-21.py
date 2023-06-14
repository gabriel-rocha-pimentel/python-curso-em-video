"""
DESENVOLVA UM PROGRAMA QUE LEIA O
NOME, IDADE E SEXO DE 4 PESSOAS.

NO FINAL DO PROGRAMA MOSTRE :

--> A MÉDIA DE IDADE DO GRUPO.

--> QUAL É O NOME DO HOMEM MAIS VELHO.

--> QUANTAS MULHERES TÊM MENOS DE 20 ANOS.




"""

print('{} \n '
      '\t\t\t\t\t\t\t\t ANALISE DE GRUPO'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

num = int(input('Escreva o número de pessoas : '))

media_idade = 0
nome = ''
idade = 0
sexo = ''
maior = 0
nome_Maisvelho = ''
mulheres = []

for pessoa in range(1, num + 1):
      print('\n=====---- {} PESSOA ----====='.format(pessoa))
      nome = input('NOME : ').upper()
      idade = int(input('Idade : '))
      sexo = input('Sexo [M | F] : ').upper()

      media_idade += idade / 4

      if pessoa == 1:
            nome_Maisvelho = nome
            maior = idade
      else:
            if sexo == 'M' and idade > maior:
                  maior = idade
                  nome_Maisvelho = nome

      if sexo == 'F' and idade <= 20:
            mulheres += [nome]
print(nome)
print('\nA média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {} '.format(maior, nome_Maisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(len(mulheres)))
