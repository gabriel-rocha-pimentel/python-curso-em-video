"""
Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido.
"""

from random import choice
aluno_01 = input('Insira aqui o nome do primeiro aluno >  ')
aluno_02 = input('Insira aqui o nome do segundo aluno > ')
aluno_03 = input('Insira aqui o nome do terceiro aluno > ')
aluno_04 = input('Insira aqui o nome do quarto aluno > ')

alunos = [aluno_01, aluno_02, aluno_03, aluno_04]

print('O nome do aluno sorteado para apagar o quadro é {}.'.format(choice(alunos)))
