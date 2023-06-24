"""
FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS,
UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO.
O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.
"""
while True:
    count = resultado = 0
    print('-' * 50)
    num = int(input('Quer ver a tabuada de qual valor ? '))
    print('-' * 50)

    if num >= 0:
        while count < 10:
            if num >= 0:
                count += 1
                resultado = num * count
                print(f'{num} X {count} = {resultado}')
    else:
        print('\nValor Invalido, logo\nPROGRAMA TABUADA ENCERRADO.')
        break
