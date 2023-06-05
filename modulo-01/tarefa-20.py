"""

Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento.

Para salários superiores a R$1.250.00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.

"""

salario = float(input('Insira aqui o seu salário para saber o seu aumento : '))

if salario <= 1250:
    print('O seu aumento é de 15% portanto você receberá R${:.2f} a mais.'.format(salario * 15 / 100))
else:
    print('O seu aumento é de 10% portanto você receberá R${:.2f} a mais.'.format(salario * 10 / 100))
