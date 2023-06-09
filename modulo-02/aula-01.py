"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

# --- TITULO ---
print('{} \n '
      '\t\t\t\t\t\t\t\t PROGRAMA DE EMPRESTIMOS'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

# --- QUESTIONÁRIO ---

# --- QUESTIONÁRIO ---

valor_casa = float(input('Qual o valor da casa : R$'))
valor = float(input('Qual é o seu salário mensal : R$'))
tempo = int(input('Por quanto tempo quer financiar : '))
prestacao_mensal = valor_casa / (tempo * 12)

salario = valor * 30 / 100

print('\nPara pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'
      .format(valor_casa, tempo, prestacao_mensal))

if prestacao_mensal <= salario:
    print("Empréstimo Concedido!!!")
else:
    print('Empréstimo Negado.')
