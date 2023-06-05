"""
Faça um programa que leia uma frase pelo teclado e mostre:

--> Quantas vezes aparece a letra 'A'.
--> Em que posição ela aparece a primeira vez.
--> Em que posição ela aparece a última vez.
"""

frase = input('Digite uma frase : ').lower().strip()

print('Sua frase tem {} letras A. \n'
      'O `A` aparece pela primeira vez na posição {}. \n'
      'E pela ultima vez na posição {}.'
      .format(frase.count('a'), frase.find('a') + 1, frase.rfind('a') + 1))
