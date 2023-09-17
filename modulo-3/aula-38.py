"""
CRIE UM PEQUENO SISTEMA MODULARZADO
QUE PERMITA CADASTRAR PESSOAS PELO SEU NOME
E IDADE EM UM ARQUIVO DE TEXTO Simples.

O SISTEMA SÓ VAI TER 2 OPÇÕES: CADASTRAR UMA NOVA
PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS
"""
from cadastro import cadastrar, listPeople

nome = input('Escreva seu nome: ')
idade = input('Escreva sua idade: ')
email = input('Escreva seu email: ')
usuario = input('Escreva seu nome de usuário: ')

try:
      people = cadastrar(nome, idade, email, usuario)
      listPeople(people)
except SyntaxError:
      print('FALHA AO EXECUTAR A FUNÇÃO DE ABRIR ARQUIVO')
else:
      print('ARQUIVO CRIADO COM SUCESSO !!!')
