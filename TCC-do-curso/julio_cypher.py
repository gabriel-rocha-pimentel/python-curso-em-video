alfabeto = ['A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X',
            'Y', 'Z']
pavras = list()
msg = str(input('Escreva a mensagem que deseja encriptar.\n>>>  ')).strip().upper()
pos_frente = int(input('Escreva o número de posições que deseja usar para codificar a mensagem : '))
for l1 in msg:
      for l2 in alfabeto:
            if l1 == l2:
                  pos = alfabeto.index(l1) + pos_frente
                  pavras += alfabeto[pos]

for letra in pavras:
      print(letra, end=' ')

print('\n'+msg)

