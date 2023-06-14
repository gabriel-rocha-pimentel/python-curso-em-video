"""
FAÇA UM PROGRAMA QUE LEIA O PESO
DE CINCO PESSOAS. NO FINAL, MOSTRANDO
QUAL FOI O MAIOR E O MENOR PESO LIDOS.
"""
# MEU CÓDIGO
print('{} \n '
      '\t\t\t\t\t\t\t\t ANALISE DE PESO - MEU PROGRAMA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

peso = 0.0
pessoas = []
media = 0
for count in range(1, 6):
      peso = float(input('Escreva o peso da {}ª pessoa : '.format(count)))
      pessoas += [peso]

print('\nO maior peso lido foi de {:.2f}Kg'.format(max(pessoas)))
print('O menor peso lido foi de {:.2f}Kg'.format(min(pessoas)))

print('\n{}\n'.format('-=-'*30))

# CÓDIGO DO PROFESSOR GUANABARA
print('{} \n '
      '\t\t\t\t\t\t\t\tANALISE DE PESO - PROFESSOR GUANABARA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))


maior = 0
menor = 0
for p in range(1, 6):
      peso = float(input('Escreva o peso da {}ª pessoa : '.format(p)))
      if p == 1:
            maior = peso
            menor = peso
      else:
            if peso > maior:
                  maior = peso
            if peso < menor:
                  menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
