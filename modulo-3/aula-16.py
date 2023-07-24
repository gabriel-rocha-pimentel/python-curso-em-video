"""
Faça um programa que ajude um jogador da MEGA SENA
a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randrange
from time import sleep

print('_' * 50)
print(f'{"+++++ JOGAR NA MEGA SENA +++++":^50}')
print('_' * 50)

num_jogos = []
num = int(input('Quantos jogos você quer que eu sorteie?\n--->>> '))
count = 1

print(f'{"-=" * 5} SORTEANDO {num} JOGOS {"=-" * 5}')

while count <= num:
    jogo = []
    while len(jogo) < 6:
        numero = randrange(1, 61)
        if numero not in jogo:
            jogo.append(numero)
    num_jogos.append(jogo)
    count += 1

for idx, jogo in enumerate(num_jogos):
    print(f'Jogo {idx+1}: {jogo}')
    sleep(1)

print(f'{"-=" * 5} < BOA SORTE > {"=-" * 5}')
