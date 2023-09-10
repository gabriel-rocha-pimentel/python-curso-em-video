"""
 FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS()
 QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E VAI
 RETORNAR UM DICIONARIO COM AS SEGUINTES INFORMAÇÕES:

 - QUANTIDADE DE NOTAS
 - A MAIOR NOTA
 - A MENOR NOTA
 - A MÉDIA DA TURMA
 - A SITUAÇÃO (OPCIOAL)

 * ADICIONE TAMBÉM AS DCSTRINGS DA FUNÇÃO.
"""


def notas(*numeros, sit=None):
      """
      => Função para analisar notas e situações dos alunos.
      :param numeros: Adicione as notas dos alunos
      :param sit: Compreende a situação atual do aluno, sit=True para BOA
      ou sit=False para RUIM.
      :return: Retorna dicionario com informações da média, total, situação, maior
      e menor notas do aluno.
      """
      ficha = dict()
      Nota = list()

      for num in numeros:
            Nota.append(num)

      tamanho = len(Nota)
      ficha.update({'notas': Nota[:]})
      ficha.update({'total': tamanho})
      ficha.update({'maior': max(Nota)})
      ficha.update({'menor': min(Nota)})
      media = sum(Nota) / tamanho
      ficha.update({'media': f'{media:2.2f}'})
      if sit:
            if media > 6:
                  sit = 'BOA'
            elif media <= 6:
                  sit = 'RUIM'
            ficha.update({'situação': sit})
      return ficha


# PROGRAMA PRINCIPAL
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
