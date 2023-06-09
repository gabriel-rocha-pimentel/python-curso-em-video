"""
A Confederação Nacional de natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""
import datetime

print('{} \n '
      '\t\t\t\t\t\t\t\t PROGRAMA DE CLASIFICAÇÃO'
      '\n {}'.format('-=-' * 30, '-=-' * 30))


ano = int(input('Escreva a data de nascimento do atleta : '))
data = datetime.date.today().year
idade = data - ano

if idade <= 9:
    print('Como você tem {} anos, sua categória é : MIRIM'.format(idade))
elif idade <= 14:
    print('Como você tem {} anos, sua categória é : INFANTIL'.format(idade))
elif idade <= 19:
    print('Como você tem {} anos, sua categória é : JUNIOR'.format(idade))
elif idade <= 25:
    print('Como você tem {} idade, sua categória é : SÊNIOR'.format(idade))
else:
    print('Como você tem {} anos, sua categória é : MASTER'.format(idade))
