"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- Á vista dinheiro/cheque: 10% de desconto
- Á vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão 20% de juros.

# E a vista no cartão tera -5% de desconto
a_vista = value - ((value * 5) / 100)

# E parcelando 2x no cartão, preço normal
dobro_no_cartao = value // 2

# Agora parcelando 3x ou mais no cartão, tem um acrescimo de 20%
triplo_cartao = (value // 3) + (value + ((value * 20) / 100))

"""

print('{} \n '
      '\t\t\t\t\t\t\t\t NERD SHOP'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

valor = int(input('Informar valor do carrinho : R$ '))

print('-=--=--=--=- FORMAS DE PAGAMENTO -=--=--=--=- \n'
      '[1] Á VISTA dinheiro ou cheque \n'
      '[2] A VISTA no cartão \n'
      '[3] 2x no CARTÃO \n'
      '[4] 3x ou mais no CARTÃO \n')
opcao = int(input('Escolha uma opção : '))

if opcao == 1:
    print('Você recebera um desconto de 10% portanto pagará apenas R${:.2f}'.format(valor - (valor * 10) / 100))
elif opcao == 2:
    print('Por ser a vista porém no cartão o desconto será de apenas 5%. \n'
          'Logo vocẽ pagará R${:.2f}.'.format(valor - (valor * 5) / 100))

elif opcao == 3:
    print('Em até 2x no cartão o valor é fixo.\n'
          'Logo você pagará duas parcelas de R${:.2f}.'.format(valor // 2))

elif opcao == 4:
    parcelas = int(input('Quantas parcelas quer pagar ? '))

    juros = valor + (valor * 20) / 100
    p = juros / parcelas

    print('Em até 3x ou mais no cartão, terá um acrescimo de 20%. \n'
          'Logo você pagará {} parcelas de R${:.2f}. \n'
          'Completando um total de {:.2f}'.format(parcelas, p, juros))
