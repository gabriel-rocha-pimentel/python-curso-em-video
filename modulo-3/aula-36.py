"""
REESCREVA A FUNÇÃO LEIAINT() QUE FIZEMOS
NO DESAFIO 104, INCLUINDO AGORA A POSSIBILIDADE
DA DIGITAÇÃO DE UM NÚMERO DE TIPO INVÁLIDO.
APROVEITE E CRIE TAMBÉM UMA FUNÇÃO LEIAFLOAT()
COM A MESMA FUNCIONALIDADE.
"""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERROR:por favor, escreva um número válido\033[m')
            continue
        else:
            return n


# PROGRAMA PRINCIPAL
numero = leiaInt('Digite um Inteiro: ')
print(f'O valor digitado foi {numero}')
