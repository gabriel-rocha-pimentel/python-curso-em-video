"""
CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VARIAS PESSOAS.
A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO
QUER OU NÃO CONTINUAR.

NO FINAL, MOSTRE:
1- QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
2- QUANTOS HOMENS FORAM CADASTRADOS.
3- QUANTAS MULHERES TEM MENOS DE 20 ANOS.
"""
print('{} \n '
      '\t\t\t\t\t\t\t\tFICHA DE CADASTRO'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

maior_18 = 0
man = 0
mulher_menor20 = 0

while True:
      idade = int(input('\nEscreva sua idade : '))
      sexo = input('Escreva [MASCULINO] ou [FEMININO] : ').strip().upper()[0]

      if idade >= 18:
            maior_18 += 1
      if sexo == 'M':
            man += 1
      if idade < 20 and sexo == 'F':
            mulher_menor20 += 1
      elif sexo != 'F' and sexo != 'M':
            print('VALOR INVALIDO !')
            continue

      opcao = input('Quer continuar ?\nEscreva [SIM | NÃO] : ').upper()[0]
      if opcao == 'S':
            continue
      elif opcao == 'N':
            break

print(f'\nO número de PESSOAS maiores de 18 é : {maior_18}.\n'
      f'E o número de HOMENS cadastrados é : {man}.\n'
      f'E por fim o número de MULHERES menores 20 é : {mulher_menor20}')
