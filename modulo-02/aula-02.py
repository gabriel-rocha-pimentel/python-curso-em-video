"""
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base da conversãp.

- Binário
- Octal
- Hexadecimal
"""

# --- TITULO ---
print('{} \n '
      '\t\t\t\t\t\t\t\t PROGRAMA DE CONVERSÃO'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

num = int(input('Escreva um número para converter : '))

conversao = input('Escolha uma base para conversão : \n'
                  'A - Bínario. \n'
                  'B - Octal.\n'
                  'C - Hexadecimal.\n'
                  '-->->->->->-> ').upper().strip()

if conversao == 'A':
    binario = (bin(num))
    print(binario[2:])

elif conversao == 'B':
    octal = (oct(num))
    print(octal[2:])

elif conversao == 'C':
    hexadecimal = (hex(num))
    print(hexadecimal[2:])

else:
    print('Número invalido por favor comece novamente.')
