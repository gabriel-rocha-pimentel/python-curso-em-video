"""
Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a
formatação correta.
"""
# MEU CÓDIGO
print('_' * 50)
print(f'{"+++++ MATRIZES EM PYTHON +++++":^50}')
print('_' * 50)
par = columm = 0
row = []
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for p1, n in enumerate(range(0, 3)):
      for p2, c in enumerate(range(0, 3)):
            value = int(input(f'Digite um valor para {p1, p2}: '))
            matriz[n][c] = value
            if p2 == 2:
                  columm += value
            if p1 == 1:
                  row.append(value)
            if value % 2 == 0:
                  par += value
            print(matriz[c])
            print(matriz[n])
print('-=' * 30)
for num in range(0, 3):
      for c in range(0, 3):
            print(f'[{matriz[num][c]:^5}]', end='')
      print()
print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {columm}.')
print(f'O maior valor da segunda linha é {max(row)}')
