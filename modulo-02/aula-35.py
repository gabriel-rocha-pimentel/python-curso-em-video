"""
CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS.
O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR.
NO FINAL, MOSTRE:

1- QUAL É O VALOR TOTAL GASTO NA COMPRA.
2- QUANTOS PRODUTOS CUSTAM MAIS DE R$1000
3- QUAL É O NOME DO PRODUTO MAIS BARATO.
"""
print('{} \n '
      '\t\t\t\t\t\t\t\tMERCEARIA DO MÁRIO'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

valor_total = maior_mil = count = barato = 0
opcao = produto_barato = ''

while True:
    nome = input('\nEscreva o nome do PRODUTO : ').strip().upper()
    valor = float(input('Escreva aqui o VALOR do produto : '))
    count += 1
    valor_total += valor

    if count == 1 or valor < barato:
        barato = valor
        produto_barato = nome

    if valor >= 1000.00:
        maior_mil += 1

    opcao = input('Quer continuar ?\n[SIM|NÃO] : ').strip().upper()[0]

    if opcao == 'S':
        continue
    elif opcao == 'N':
        print('{} FIM DA COMPRA {}'.format('-=-'*15, '-=-'*15))
        break

print(f'\nO produto mais barato é {produto_barato}')
print(f'O número de produtos maiores de 1000.00 é {maior_mil}')
print(f'O valor total gasto foi R${valor_total} REAIS.')
