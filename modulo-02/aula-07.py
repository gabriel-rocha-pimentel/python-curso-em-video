"""
Refaça o Desafio dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes.
"""

print('{} \n '
      '\t\t\t\t\t\t\t\t DESAFIO DOS TRIÂNGULOS'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

a = float(input('Primeiro lado do triângulo : '))
b = float(input('Segundo lado do truângulo : '))
c = float(input('Terceiro lado do triãngulo : '))

if a < b + c and b < a + c and c < a + b:
    print('Podem formar um triângulo. ', end='')
    if a == b == c:
        print('EQUILATERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')

else:
    print('NÃO podem formar um triângulo')
