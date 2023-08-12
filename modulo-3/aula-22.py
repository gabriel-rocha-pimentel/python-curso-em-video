"""
Crie um programa que leia nome, idade e sexo
de várias pessoas, guardando os dados de cada pessoa
em um dicionario e todos os dicionarios em uma lista.
Para no fim mostrar :

a - Quantas pessoas foram cadastradas
b - A média de idade do grupo
c - Uma lista com todas as mulheres
d - Uma lista com todas as pessoas com idade acima da média.


for k, v in pessoa.items():
      print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
      print(f'B) A média de idade é de {})

"""
print('_' * 50)
print(f'{"+++++ UNINDO DICIONARIOS E LISTAS +++++":^50}')
print('_' * 50)

pessoas = list()
pessoa = dict()
sexo = ''
idade = 0

while True:
      pessoa.update({'nome': input('NOME: ').strip()})
      while True:
            sexo = input('SEXO - [M ou F]\n>>> ').strip().upper()[0]
            if sexo != 'M' and sexo != 'F':
                  print('ERROR !Por favor, digite apenas M ou F.')
            else:
                  pessoa.update({'sexo': sexo})
                  break
      pessoa.update({'idade': int(input('IDADE: '))})
      idade += pessoa["idade"]
      pessoas.append(pessoa.copy())
      stop = input("Quer continuar ? [SIM ou NÃO]\n>>> ").strip().upper()[0]

      if stop == 'N':
            break
      if stop == 'S':
            continue
      else:
            print('ERROR ! Digite SIM ou NÃO.')

print('-=' * 50)
media = idade / len(pessoas)

print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for pessoa in pessoas:
      if pessoa["sexo"] == 'F':
            print(pessoa["nome"], end=', ')
print('\nD) Lista das pessoas que estão acima da média: ')
for pessoa in pessoas:
      if pessoa["idade"] >= media:
            for chave, valor in pessoa.items():
                  print(f'{chave} = {valor}; ')
print('<< ENCERRADO >>')
