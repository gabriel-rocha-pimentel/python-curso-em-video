"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0:
REPROVADO

- Média entre 5.0 e 6.9:
RECUPERAÇÃO

- Média 7.0 ou superior:
APROVADO
"""

print('{} \n '
      '\t\t\t\t\t\t\t\t\t PROGRAMA DE NOTAS ESCOLAR'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

n1 = float(input('Escreva aqui a primeira nota : '))
n2 = float(input('Escreva aqui a segunda nota : '))

media = (n1 + n2) / 2

if media <= 5.0:
    print('\n REPROVADO :(')
    print('Sua nota foi {}, lembre-se de estudar bastante na próxima.'.format(media))
elif 5.0 < media <= 6.9:
    print('\n RECUPERAÇÃO :| ')
    print('Sua nota foi {}, desta vez foi por pouco, precisa estudar mais.'.format(media))
else:
    print('\n APROVADO !!! :)')
    print('Sua nota foi {}, esse é o fruto do seu esforço e dedicação. PARABÉNS !!!'.format(media))
