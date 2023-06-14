"""
FAÇA UM PROGRAMA QUE MOSTRE NA TELA
UMA CONTAGEM REGRESSIVA PARA O
ESTOURO DE FOGOS DE ARTIFICIO,
INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1
SEGUNDO ENTRE ELAS.
"""
from time import sleep
print('{} \n '
      '\t\t\t\t\t\t\t\t CONTAGEM REGRESIVA'
      '\n {}'.format('-=-' * 30, '-=-' * 30))

for c in range(10, 0, -1):
      print(c)
      sleep(1)
print('BUM!', end=' ')
sleep(1)
print('BUM!', end=' ')
sleep(1)
print('POOOW!')
