"""
Crie um programa que leia nome e duas notas
de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um
e permita que o susuário possa mostrar as notas
de cada aluno indiviadulmente.
"""
# Meu código
info_aluno = []

print('_' * 50)
print(f'{"+++++ BOLETIM ESCOLAR +++++":^50}')
print('_' * 50)

while True:
      nota_alunos = []
      nome = str(input('\nNome : '))
      nota_alunos.append(nome)

      for n in range(1, 3):
            nota = float(input(f'Nota {n}: '))
            nota_alunos.append(nota)

      parar = input('Quer continuar ? [SIM ou NÃO]\n>>> ').strip().upper()[0]
      info_aluno.append(nota_alunos[:])
      nota_alunos.clear()

      if parar == 'N':
            break

print('-=' * 30)
print('No.   NOME        MÉDIA')
print('-' * 50)

for count in range(len(info_aluno)):
      print(count, end='   ')
      print(info_aluno[count][0], end='        ')
      media = (info_aluno[count][1] + info_aluno[count][2]) / 2
      print(media)
aluno = 0

while aluno != 999:
      aluno = int(input('\nMostrar nota de qual aluno ? (999 interrompe): '))
      for i in range(len(info_aluno)):
            if aluno == i:
                  print(f'Notas de {info_aluno[aluno][0]} são {info_aluno[aluno][-2:]}')
print('<<< VOLTE SEMPRE >>>')

# CÓDIGO DO PROFESSOR GUANABARA
ficha = list()
while True:
      nome = str(input('Nome: '))
      nota1 = float(input('Nota 1: '))
      nota2 = float(input('Nota 2: '))
      media = (nota1 + nota2) / 2
      ficha.append([nome, [nota1, nota2], media])
      resp = str(input('Quer continuar? [D/N] '))
      if resp in 'Nn':
            break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
      print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
      print('-' * 35)
      opc = int(input('Mostar notas de qual aluno ? (999 interrompe): '))
      if opc == 999:
            print('FINALIZANDO...')
            break
      if opc <= len(ficha) - 1:
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
