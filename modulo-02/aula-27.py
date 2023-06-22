"""
PERGUTE PARA O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS
TERMOS. O PROGRAMA ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.
"""
import time

print('*{}*\n '
      '\t\t\t\t\t\t\t\t GERADOR DE PA'
      '\n*{}*'.format('-+-' * 30, '-+-' * 30))

play = input('Para iniciar o programa Press [S] para terminar Press [F]\n'
             'Escreva sua opção >>> ').upper()

if play == 'S':
    termo = int(input('Escreva o primeiro termo : '))
    razao = int(input('Escreva a Razão também : '))

    copia = 0
    count_more = 10
    while count_more != 0:
        copia += count_more
        count = 1
        while count <= count_more:  # <-- Termos a mais
            print(termo, end=' --> ')
            count += 1
            termo += razao
        print('PAUSA')
        count_more = int(input('Quantos termos a mais quer mostrar ? '))
    print('Progressão finalizada com {} termos mostrados.'.format(copia))

    print('\nFinalizando', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Programa Encerrado!')

elif play == 'F':
    print('\nFinalizando', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Programa Encerrado!')
else:
    print('Opção invalída! TENTE NOVAMENTE')
