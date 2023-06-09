"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

print('{} \n '
      '\t\t\t\t\t\t\t\t PROGRAMA - FAIXA DE PESO'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

altura = float(input('Escreva sua altura em metros : '))
peso = float(input('Escreva o seu peso em Kg : '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Seu IMC é {:.2f}. \n'
          'Portanto você está abaixo do peso.'.format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é {:.2f}. \n'
          '\033[0;32mLogo seu peso é ideal.'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é {:.2f}. \n'
          '\033[0;33mEntão você está sobrepeso.'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é {:.2f}. \n'
          '\033[0;33mCUIDADO! Você chegou a obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f}. AVISO!!! Você está com Obesidade Morbida. \n'
          '\033[0;31mO Ministério da Saúde adverte, OBESIDADE MORBIDA pode levar a MORTE.'.format(imc))
