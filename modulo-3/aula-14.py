"""
Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e impares. No final, mostre os valores
pares e impares em ordem crescente.
"""
print('_' * 50)
print(f'{"+++++ LISTA COM PARES E IMPARES +++++":^50}')
print('_' * 50)
numbers = [[], []]

for count in range(1, 7):
      value = int(input(f'Digite o valor {count}o. Valor: '))

      if value % 2 == 0:
            numbers[0].append(value)
      else:
            numbers[1].append(value)

par = sorted(numbers[0])
impar = sorted(numbers[1])

print('-=' * 30)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')
