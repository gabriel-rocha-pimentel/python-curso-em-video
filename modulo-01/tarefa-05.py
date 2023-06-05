"""
O mesmo professor do desafio anterior quer sortear a ordem
de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome e mostre a ordem sorteada.
"""
from random import shuffle

aluno_01 = input('Insira aqui o nome do primeiro aluno >  ')
aluno_02 = input('Insira aqui o nome do segundo aluno > ')
aluno_03 = input('Insira aqui o nome do terceiro aluno > ')
aluno_04 = input('Insira aqui o nome do quarto aluno > ')

lista = [aluno_01, aluno_02, aluno_03, aluno_04]
shuffle(lista)
print('A ordem será : {}'.format(lista))
