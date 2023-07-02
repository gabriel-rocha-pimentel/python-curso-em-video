"""
CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA
DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORFEM DE COLOCAÇÃO.
DEPOIS MOSTRE:

- APENAS OS 5 PRIMEIROS COLOCADOS.
- OS ÚLTIMOS 4 COLOCADOS DA TABELA.
- UMA LISTA COM OS TIMES EM ORFEM ALFABETICA
- EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE.
"""
print('_' * 50)
print('\t\t\t++++++ TIMES DE FUTEBOL ++++++')
print('_' * 50)

times = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Fluminense',
         'Internacional', 'Bragantino', 'Fortaleza', 'Atletico-PR', 'Atletico-MG',
         'São Paulo', 'Cruzeiro', 'Santos', 'Bahia', 'Corinthians',
         'Cuiaba', 'Góias', 'Vasco da Gama', 'America-MG', 'Coritiba')
num = 0
print('\nLista de times do Brasileirão : ')
for c in times:
    num += 1
    print(f'{num}º - ' + c + ',')

print('\nTimes em ordem alfabetica :')
for c in sorted(times):
    print(c + ',')

print('\nOs 5 primeiros são :', end='')
for c in times[:5]:
    print(c, end=', ')

print('\nOs 4 últimos são :', end='')
for c in times[-4:]:
    print(c, end=', ')

print(f'\n\nO time de Cuiaba está na {times.index("Cuiaba")}º posição.')
print('__'*30)

print('\nFIM DA EXECUÇÃO DO PROGAMA...')
