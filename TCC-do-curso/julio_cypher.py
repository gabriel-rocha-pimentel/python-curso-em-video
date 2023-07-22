alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
palavras = []
mensagem = input('Escreva a mensagem que deseja encriptar:\n>>> ').strip().upper()
pos_frente = int(input('Escreva o número de posições que deseja usar para codificar a mensagem: '))

# Codificando a mensagem usando a função maketrans()
tabela_codificacao = str.maketrans(alfabeto, alfabeto[pos_frente:] + alfabeto[:pos_frente])
mensagem_codificada = mensagem.translate(tabela_codificacao)

# Imprimindo a mensagem codificada
print('Mensagem codificada:', mensagem_codificada)

