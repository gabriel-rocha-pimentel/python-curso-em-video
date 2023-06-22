"""
FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE
OS VALORES M OU F. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE
ATÉ TER UM VALOR CORRETO.
"""

print('{} \n '
      '\t\t\t\t\t\t\t\t VALIDAÇÃO DE DADOS'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

sexo = input('Informe seu sexo >>> [M | F] : ').upper().strip()[0]

while sexo != 'M' and sexo != 'F':
      sexo = input('Dados inválidos. Por favor informe o sexo novamente : ').upper().strip()[0]

print('Sexo {} registrado com sucesso!!'.format(sexo))
